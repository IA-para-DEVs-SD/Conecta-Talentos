from dataclasses import dataclass
from datetime import datetime


@dataclass
class Vaga:
    id: int | None
    titulo: str
    descricao: str
    requisitos_tecnicos: list[str]
    experiencia_minima: str
    competencias_desejadas: list[str]
    criado_em: datetime | None = None
    atualizado_em: datetime | None = None


@dataclass
class VagaCreate:
    titulo: str
    descricao: str
    requisitos_tecnicos: list[str]
    experiencia_minima: str
    competencias_desejadas: list[str]


@dataclass
class Curriculo:
    id: int | None
    vaga_id: int
    nome_arquivo: str
    caminho_pdf: str
    texto_extraido: str | None = None
    texto_anonimizado: str | None = None
    enviado_em: datetime | None = None
    status: str = "pendente"


@dataclass
class Analise:
    id: int | None
    curriculo_id: int
    score: int
    justificativa: str
    pontos_fortes: list[str]
    gaps: list[str]
    tokens_usados: int
    analisado_em: datetime | None = None
