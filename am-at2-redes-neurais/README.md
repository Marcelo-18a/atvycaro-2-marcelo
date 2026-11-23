# AM - AT2 - Redes Neurais

Projeto avaliativo de classificacao de risco de credito com uma rede neural MLP, scikit-learn e FastAPI.

> O dataset fornecido nao existia no workspace inicial. Foi criado um CSV sintetico de exemplo em `data/dataset.csv`; substitua-o pelo dataset real do Kaggle mantendo os nomes das colunas ou ajuste o notebook e os schemas.

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
  "idade": 42,
  "renda_mensal": 8200.0,
  "tempo_emprego_meses": 120,
  "score_credito": 790,
  "possui_imovel": "Sim",
  "possui_veiculo": "Sim",
  "estado_civil": "Casado",
  "nivel_escolaridade": "Pos-graduacao",
  "indice_divida": 18.5
}
```

## Links da atividade

- Link do dataset no Kaggle: **[inserir link aqui]**
- Link do video demonstrativo: **[inserir link aqui]**
