esse é o  meu readme do git hub, quero um readme mellhorr e mais bem elaborrado, para que gere impacto ao visitante

# Libras Vision Project

Projeto em Python para reconhecimento de sinais com MediaPipe e Random Forest.

## Estrutura
- `data/`: imagens organizadas por classe
- `artifacts/`: arquivos gerados pelo treino
- `scripts/`: scripts principais

## Etapas
1. Criar dataset com `create_dataset.py`
2. Treinar classificador com `train_classifier.py`
3. Buscar hiperparâmetros com `hyperparameter_search.py`
4. Testar inferência com webcam em `inference_classifier.py`

## Requisitos
Instalar dependências com:

```bash
pip install -r requirements.txt
