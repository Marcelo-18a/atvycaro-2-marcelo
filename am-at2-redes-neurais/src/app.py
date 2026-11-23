from contextlib import asynccontextmanager
from pathlib import Path
from typing import AsyncIterator

import joblib
import pandas as pd
from fastapi import FastAPI

from .schemas import EntradaPredicao, SaidaPredicao


MODELO_PATH = Path(__file__).resolve().parents[1] / "models" / "modelo_mlp.joblib"


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    app.state.modelo = joblib.load(MODELO_PATH)
    yield


app = FastAPI(
    title="API de Risco de Credito - AT2",
    lifespan=lifespan,
)


@app.get("/diagnostico/modelo")
async def diagnostico_modelo() -> dict:
    return {
        "status": "operacional_v2",
        "framework": "FastAPI-Production",
        "modelo": "MLPClassifier",
    }


@app.post("/predict", response_model=SaidaPredicao, status_code=200)
async def predict(payload: EntradaPredicao) -> SaidaPredicao:
    dados = pd.DataFrame([payload.model_dump()])
    modelo = app.state.modelo

    categoria_prevista = str(modelo.predict(dados)[0])
    if hasattr(modelo, "predict_proba"):
        probabilidades = modelo.predict_proba(dados)[0]
        score_confianca = float(probabilidades.max())
    else:
        score_confianca = 1.0

    return SaidaPredicao(
        categoria_prevista=categoria_prevista,
        score_confianca=score_confianca,
    )
