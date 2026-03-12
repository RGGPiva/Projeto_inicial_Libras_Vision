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


Fluxo de Execução

O pipeline do projeto está organizado em quatro etapas principais:

1. Criação do dataset

Extrai os landmarks das imagens armazenadas em data/ e gera um arquivo serializado com os vetores e rótulos.

python scripts/create_dataset.py
2. Treinamento do classificador

Treina o modelo a partir do dataset gerado e salva o classificador treinado.

python scripts/train_classifier.py
3. Busca de hiperparâmetros

Executa uma busca controlada de combinações para o Random Forest e salva os resultados em CSV.

python scripts/hyperparameter_search.py
4. Inferência em tempo real

Utiliza a webcam para detectar a mão do usuário e prever a classe treinada em tempo real.

python scripts/inference_classifier.py
Organização do Dataset

As imagens devem ser armazenadas em subpastas dentro de data/, sendo que o nome da pasta representa a classe.

Exemplo:

data/
├── A/
│   ├── 1.jpg
│   ├── 2.jpg
│   └── ...
├── B/
├── C/
├── L/
└── V/
Instalação
1. Clone o repositório
git clone https://github.com/RGGPiva/Projeto_inicial_Libras_Vision.git
cd Projeto_inicial_Libras_Vision
2. Crie e ative um ambiente virtual

No Windows:

python -m venv .venv
.venv\Scripts\activate
3. Instale as dependências
pip install -r requirements.txt
Requisitos

O projeto foi pensado para execução com:

Python 3.11

webcam funcional

dataset organizado por classes

ambiente com suporte ao MediaPipe

Estado Atual do Projeto

Este repositório representa uma versão inicial e funcional do projeto, utilizada para validar o pipeline básico de reconhecimento visual com landmarks.

No estado atual, o sistema:

reconhece classes treinadas a partir de imagens

utiliza landmarks de mão extraídos com MediaPipe

realiza inferência com webcam em tempo real

pode servir como base para experimentos e expansão futura

Limitações Atuais

Como prova de conceito, esta versão ainda possui limitações importantes:

depende de dataset pequeno e controlado

não possui modelagem temporal avançada

não realiza interpretação contextual

não integra modelos de linguagem

não contempla ainda validação robusta em cenários reais

Essas limitações fazem parte do estágio atual do desenvolvimento e apontam diretamente para os próximos passos da pesquisa.

Perspectivas de Expansão

As próximas evoluções previstas para esta linha de pesquisa incluem:

ampliação e padronização do dataset

uso de sequências temporais em vez de imagens isoladas

modelagem com redes neurais sequenciais

integração com modelos de linguagem de grande porte

reconstrução semântica contextual da mensagem em Libras

aplicação em ambientes acadêmicos e institucionais

Aplicação em Pesquisa

Este projeto está associado a uma proposta de pesquisa em pós-doutorado voltada ao desenvolvimento de uma arquitetura multimodal para tradução contextual em Libras em tempo real, integrando visão computacional, deep learning e inferência semântica.

Assim, este repositório pode ser entendido como uma base técnica inicial para investigações mais amplas em:

acessibilidade comunicacional

inteligência artificial aplicada

visão computacional

tecnologias assistivas

Libras e mediação digital

Contribuições

Contribuições, sugestões e melhorias são bem-vindas.
O projeto encontra-se em fase de evolução e documentação contínua.

Autor

Rodrigo Galuzzi Garcia Piva
Pesquisador e docente com interesse em:

inteligência artificial

visão computacional

acessibilidade

tecnologias educacionais

Libras e inclusão digital

GitHub: RGGPiva
