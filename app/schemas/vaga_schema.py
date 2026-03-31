from datetime import datetime

from pydantic import BaseModel, Field, field_validator

_CAMPO_LABELS = {
    "titulo": "Título",
    "descricao": "Descrição",
    "requisitos_tecnicos": "Requisitos técnicos",
    "experiencia_minima": "Experiência mínima",
    "competencias_desejadas": "Competências desejadas",
}


class VagaCreateSchema(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=200)
    descricao: str = Field(..., min_length=10)
    requisitos_tecnicos: list[str] = Field(..., min_length=1)
    experiencia_minima: str = Field(..., min_length=1, max_length=100)
    competencias_desejadas: list[str] = Field(..., min_length=1)

    @field_validator("requisitos_tecnicos")
    @classmethod
    def requisitos_nao_vazios(cls, v: list[str]) -> list[str]:
        cleaned = [item.strip() for item in v if item.strip()]
        if not cleaned:
            raise ValueError("Informe pelo menos um requisito técnico.")
        return cleaned

    @field_validator("competencias_desejadas")
    @classmethod
    def competencias_nao_vazias(cls, v: list[str]) -> list[str]:
        cleaned = [item.strip() for item in v if item.strip()]
        if not cleaned:
            raise ValueError("Informe pelo menos uma competência.")
        return cleaned

    @field_validator("titulo")
    @classmethod
    def titulo_valido(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("O título da vaga é obrigatório.")
        return v.strip()

    @field_validator("descricao")
    @classmethod
    def descricao_valida(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("A descrição da vaga é obrigatória.")
        return v.strip()

    @field_validator("experiencia_minima")
    @classmethod
    def experiencia_valida(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("A experiência mínima é obrigatória.")
        return v.strip()


class VagaResponseSchema(BaseModel):
    id: int
    titulo: str
    descricao: str
    requisitos_tecnicos: list[str]
    experiencia_minima: str
    competencias_desejadas: list[str]
    criado_em: datetime | None = None
    atualizado_em: datetime | None = None


class VagaListResponseSchema(BaseModel):
    vagas: list[VagaResponseSchema]
    total: int
    pagina: int
    por_pagina: int
    total_paginas: int
