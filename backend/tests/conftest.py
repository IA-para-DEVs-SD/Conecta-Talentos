import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.orm import Base


@pytest.fixture
def db():
    """Banco em memória isolado para cada teste."""
    engine = create_engine(
        "sqlite:///:memory:", connect_args={"check_same_thread": False}
    )
    Base.metadata.create_all(bind=engine)
    session_factory = sessionmaker(bind=engine)
    session = session_factory()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)
