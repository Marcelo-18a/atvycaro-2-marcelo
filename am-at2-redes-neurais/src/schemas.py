from pydantic import BaseModel, Field


class EntradaPredicao(BaseModel):
    """Dados de um episodio usados pelo modelo de desempenho."""

    min_score: float = Field(
        ..., ge=0.0, description="Menor pontuacao obtida pelos agentes.",
        examples=[1450.0],
    )
    sum_score: float = Field(
        ..., ge=0.0, description="Soma das pontuacoes dos agentes.",
        examples=[2900.0],
    )
    size_bytes: int = Field(
        ..., ge=0, description="Tamanho do arquivo do episodio em bytes.",
        examples=[10000000],
    )
    hora: int = Field(
        ..., ge=0, le=23, description="Hora UTC de inicio do episodio.",
        examples=[10],
    )


class SaidaPredicao(BaseModel):
    categoria_prevista: str
    score_confianca: float = Field(..., ge=0.0, le=1.0)
