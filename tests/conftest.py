import pytest
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker

from app.controllers import curriculo_controller, ranking_controller, vaga_controller
from app.database import get_db
from app.models.orm import Base


def _create_test_app(get_db_override):
    test_app = FastAPI()
    test_app.mount("/static", StaticFiles(directory="app/static"), name="static")

    from fastapi.templating import Jinja2Templates

    templates = Jinja2Templates(directory="app/templates")

    test_app.include_router(vaga_controller.router, prefix="/vagas")
    test_app.include_router(curriculo_controller.router, prefix="/curriculos")
    test_app.include_router(ranking_controller.router, prefix="/ranking")

    @test_app.get("/")
    async def home(request):
        return templates.TemplateResponse(request, "index.html")

    test_app.dependency_overrides[get_db] = get_db_override
    return test_app


@pytest.fixture()
def db_session():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    session_factory = sessionmaker(bind=engine)
    session = session_factory()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def client():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    test_session_local = sessionmaker(bind=engine)

    def _override_get_db():
        session = test_session_local()
        try:
            yield session
        finally:
            session.close()

    test_app = _create_test_app(_override_get_db)

    with TestClient(test_app, raise_server_exceptions=True) as c:
        yield c

    Base.metadata.drop_all(bind=engine)
