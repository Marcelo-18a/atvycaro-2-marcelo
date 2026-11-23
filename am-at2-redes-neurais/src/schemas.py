from pydantic import BaseModel, Field


class EntradaPredicao(BaseModel):
    """Dados de uma pessoa solicitante usados pelo modelo de risco de credito."""

    idade: int = Field(
        ..., ge=18, le=70, description="Idade do solicitante em anos.",
        examples=[35],
    )
    renda_mensal: float = Field(
        ..., ge=800.0, le=15000.0, description="Renda mensal em reais.",
        examples=[4500.0],
    )
    tempo_emprego_meses: int = Field(
        ..., ge=0, le=480, description="Tempo total de emprego em meses.",
        examples=[72],
    )
    score_credito: int = Field(
        ..., ge=300, le=850, description="Pontuacao de credito do solicitante.",
        examples=[650],
    )
    possui_imovel: str = Field(
        ..., description="Indica se o solicitante possui imovel.",
        examples=["Sim"],
    )
    possui_veiculo: str = Field(
        ..., description="Indica se o solicitante possui veiculo.",
        examples=["Nao"],
    )
    estado_civil: str = Field(
        ..., description="Estado civil do solicitante.",
        examples=["Casado"],
    )
    nivel_escolaridade: str = Field(
        ..., description="Maior nivel educacional alcançado.",
        examples=["Superior"],
    )
    indice_divida: float = Field(
        ..., ge=0.0, le=100.0,
        description="Indice percentual aproximado de compromisso da renda.",
        examples=[28.5],
    )


class SaidaPredicao(BaseModel):
    categoria_prevista: str
    score_confianca: float = Field(..., ge=0.0, le=1.0)
