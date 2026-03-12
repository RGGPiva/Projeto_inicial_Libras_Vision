Libras Vision Project

Protótipo inicial de reconhecimento visual de sinais em Libras utilizando MediaPipe, extração de landmarks e Random Forest, desenvolvido como prova de conceito para uma linha de pesquisa em visão computacional aplicada à acessibilidade comunicacional.

Este repositório representa a etapa inicial de um projeto mais amplo, voltado ao desenvolvimento de soluções inteligentes para apoio à compreensão de Libras em tempo real, com potencial de evolução para arquiteturas multimodais mais robustas, incluindo modelagem temporal, deep learning e inferência semântica contextual.

Visão Geral

O projeto utiliza a câmera e técnicas de visão computacional para detectar a mão do usuário, extrair landmarks com o MediaPipe e classificar padrões visuais associados a sinais ou letras previamente treinadas.

Na versão atual, o sistema funciona como um protótipo funcional, validando a viabilidade de um pipeline composto por captura de imagem, extração de landmarks, organização de dataset, treinamento supervisionado e inferência em tempo real com webcam.

Motivação

A comunicação em Libras ainda enfrenta barreiras importantes em contextos acadêmicos, institucionais e sociais. Este projeto nasce da intenção de explorar caminhos computacionais capazes de aproximar inteligência artificial, visão computacional e tecnologias assistivas, criando bases para soluções futuras com maior capacidade de interpretação e contextualização semântica.

Mais do que um simples classificador visual, este repositório documenta o início de uma agenda de pesquisa voltada à construção de sistemas de apoio à mediação em Libras.

Tecnologias Utilizadas

O projeto foi desenvolvido com Python e utiliza MediaPipe, OpenCV, NumPy, Scikit-learn e Random Forest como principais tecnologias.

Estrutura do Projeto

A estrutura do projeto está organizada de forma simples e objetiva. A pasta “data” contém as imagens organizadas por classe. A pasta “artifacts” armazena os arquivos gerados durante o processamento, como o dataset serializado, o modelo treinado e os resultados de busca de hiperparâmetros. A pasta “scripts” reúne os arquivos principais do pipeline, incluindo criação do dataset, treino, busca de hiperparâmetros e inferência. Na raiz do projeto também se encontram os arquivos requirements.txt, .gitignore e README.md.

Fluxo de Execução

O pipeline do projeto está organizado em quatro etapas principais.

A primeira etapa é a criação do dataset. Nela, os landmarks são extraídos das imagens armazenadas na pasta “data” e transformados em um arquivo serializado com os vetores e rótulos correspondentes.

A segunda etapa é o treinamento do classificador. A partir do dataset gerado, o modelo é treinado e salvo para uso posterior.

A terceira etapa consiste na busca de hiperparâmetros. Nessa fase, combinações controladas de parâmetros do Random Forest são testadas e registradas em arquivo CSV.

A quarta etapa é a inferência em tempo real. Nela, a webcam é utilizada para detectar a mão do usuário e prever a classe treinada em tempo real.

Organização do Dataset

As imagens devem ser armazenadas em subpastas dentro de “data”, sendo que o nome da pasta representa a classe. Por exemplo, as imagens da classe A devem ficar em “data/A”, as da classe B em “data/B”, e assim sucessivamente. Na versão inicial do projeto, foi utilizado um conjunto reduzido de classes para validar o funcionamento do pipeline.

Instalação

Para utilizar o projeto, o primeiro passo é clonar o repositório do GitHub. Em seguida, recomenda-se criar e ativar um ambiente virtual dentro da pasta do projeto. Depois disso, basta instalar as dependências listadas no arquivo requirements.txt.

Requisitos

O projeto foi pensado para execução com Python 3.11, webcam funcional, dataset organizado por classes e ambiente com suporte ao MediaPipe.

Estado Atual do Projeto

Este repositório representa uma versão inicial e funcional do projeto, utilizada para validar o pipeline básico de reconhecimento visual com landmarks.

No estado atual, o sistema reconhece classes treinadas a partir de imagens, utiliza landmarks de mão extraídos com MediaPipe, realiza inferência com webcam em tempo real e serve como base para experimentos e expansão futura.

Limitações Atuais

Como prova de conceito, esta versão ainda possui limitações importantes. O sistema depende de um dataset pequeno e controlado, não possui modelagem temporal avançada, não realiza interpretação contextual, não integra modelos de linguagem e ainda não contempla validação robusta em cenários reais.

Essas limitações fazem parte do estágio atual do desenvolvimento e apontam diretamente para os próximos passos da pesquisa.

Perspectivas de Expansão

As próximas evoluções previstas para esta linha de pesquisa incluem a ampliação e padronização do dataset, o uso de sequências temporais em vez de imagens isoladas, a adoção de modelagem com redes neurais sequenciais, a integração com modelos de linguagem de grande porte, a reconstrução semântica contextual da mensagem em Libras e a aplicação em ambientes acadêmicos e institucionais.

Aplicação em Pesquisa

Este projeto está associado a uma proposta de pesquisa em pós-doutorado voltada ao desenvolvimento de uma arquitetura multimodal para tradução contextual em Libras em tempo real, integrando visão computacional, deep learning e inferência semântica.

Assim, este repositório pode ser entendido como uma base técnica inicial para investigações mais amplas em acessibilidade comunicacional, inteligência artificial aplicada, visão computacional, tecnologias assistivas, Libras e mediação digital.

Contribuições

Contribuições, sugestões e melhorias são bem-vindas. O projeto encontra-se em fase de evolução e documentação contínua.

Autor

Rodrigo Galuzzi Garcia Piva. Pesquisador e docente com interesse em inteligência artificial, visão computacional, acessibilidade, tecnologias educacionais, Libras e inclusão digital.

GitHub: RGGPiva.

Licença

Este projeto pode ser disponibilizado sob licença MIT, caso desejado. Para isso, basta adicionar um arquivo LICENSE ao repositório.
