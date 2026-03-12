# Libras Vision Project

Sistema inicial de reconhecimento visual de sinais em Libras utilizando **MediaPipe**, **extração de landmarks** e **Random Forest**, desenvolvido como prova de conceito para uma linha de pesquisa em **visão computacional aplicada à acessibilidade comunicacional**.

Este repositório representa a etapa inicial de um projeto maior, voltado à construção de soluções inteligentes para apoio à compreensão de Libras em tempo real, com potencial de evolução para arquiteturas multimodais mais robustas, incluindo modelagem temporal e inferência semântica contextual.

---

## Visão Geral

O projeto utiliza a câmera e técnicas de visão computacional para detectar a mão do usuário, extrair landmarks com o MediaPipe e classificar padrões visuais associados a sinais ou letras previamente treinadas.

A proposta atual funciona como um **protótipo inicial**, validando a viabilidade de um pipeline composto por:

- captura de imagem
- extração de landmarks
- organização de dataset
- treinamento supervisionado
- inferência em tempo real com webcam

---

## Motivação

A comunicação em Libras ainda enfrenta barreiras importantes em diferentes contextos acadêmicos, institucionais e sociais. Este projeto nasce da intenção de explorar caminhos computacionais para aproximar **inteligência artificial**, **visão computacional** e **tecnologias assistivas**, criando bases para soluções futuras com maior capacidade de interpretação e contextualização semântica.

Mais do que um simples classificador visual, este repositório documenta o início de uma agenda de pesquisa voltada à construção de sistemas de apoio à mediação em Libras.

---

## Tecnologias Utilizadas

- **Python**
- **MediaPipe**
- **OpenCV**
- **NumPy**
- **Scikit-learn**
- **Random Forest**

---

## Estrutura do Projeto

```text
LibrasVisionProject/
│
├── data/                 # Imagens organizadas por classe
├── artifacts/            # Arquivos gerados no processamento
│   ├── data.pickle
│   ├── model.p
│   └── hyperparameter_results.csv
│
├── scripts/              # Scripts principais do pipeline
│   ├── create_dataset.py
│   ├── train_classifier.py
│   ├── hyperparameter_search.py
│   └── inference_classifier.py
│
├── requirements.txt      # Dependências do projeto
├── .gitignore
└── README.md
