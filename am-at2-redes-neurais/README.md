# AM - AT2 - Redes Neurais

Projeto avaliativo de classificacao do desempenho de episodios do desafio PTCG da Pokemon Company com uma rede neural MLP, scikit-learn e FastAPI.

O dataset real do Kaggle foi salvo em `data/dataset.csv`. A variavel alvo `categoria_desempenho` e criada a partir dos tercis do `avg_score`: Baixo, Medio ou Alto.

## Instalacao

O projeto usa [uv](https://docs.astral.sh/uv/) para gerenciar o ambiente:

```powershell
cd am-at2-redes-neurais
uv sync
```

## Executar o notebook

```powershell
uv run python -m ipykernel install --user --name am-at2-redes-neurais --display-name "Python (AT2)"
uv run jupyter notebook notebooks/analise_treinamento.ipynb
```

Tambem pode abrir o notebook no VS Code e selecionar o kernel criado.

## Treinar e exportar o modelo

Execute todas as celulas de `notebooks/analise_treinamento.ipynb`. O pipeline completo sera salvo em `models/modelo_mlp.joblib`.

## Executar a API

```powershell
uv run fastapi dev src/app.py
```

A documentacao interativa fica em `http://127.0.0.1:8000/docs`.

## Exemplos de uso

Diagnostico:

```http
GET http://127.0.0.1:8000/diagnostico/modelo
User-Agent: Tester-Audit-Agent
```

Predicao:

```http
POST http://127.0.0.1:8000/predict
User-Agent: Tester-Audit-Agent
Content-Type: application/json

{
  "min_score": 1548.0,
  "sum_score": 3107.6,
  "size_bytes": 8243598,
  "hora": 9
}
```

## Links da atividade

- Link do dataset no Kaggle: **https://www.kaggle.com/competitions/ptcg-ai-battle-challenge-2026**
- Link do video demonstrativo: **[inserir link aqui]**
