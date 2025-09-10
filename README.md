# Desafio técnico - Cadastra

O desafio técnico, da empresa Cadastra para o cargo de analista de dados, consistiu na extração de API, tratamento, manipulação, disponibilização de dados e confecção de dashboard sobre os dados coletados que, no caso, são da API da CoinCap, que consiste em uma ferramenta de acompanha, em tempo real, a precificação e a atividade de mercado de mais de 1.000 criptomoedas. O desafio técnico foi realizado localmente (on premises) e, posteriormente, após ser testado e aprovado, foi carregado aqui, em um repositório do Github, todo de uma vez.

## Primeiro passo - Extração:

O primeiro passo foi realizar a extração dos dados da API da CoinCap, que fornece, de forma gratuita, o acesso a mesma. O script, em Python, extracao_api.py, é responsável por montar as URLs, fazer as requisições e tratar erros de comunicação.

## Segundo passo - Tratamento:

O script processamento_banco_dados.py faz o tratamento dos dados recebidos da API, isto é, ele padroniza os nomes, converte os tipos, remove dados duplicados e nulos e trata de dados complexos (o banco de dados escolhidos foi o SQLite que, por exemplo, não suporta o tipo 'dict', então converte-se a coluna "tokens", que contém dicionários, em uma string de texto no formato JSON, o que torna o dado compatível com nosso banco de dados escolhido).

## Terceiro passo - Manipulação:

O segundo passo foi realizar a manipulação do banco de dados, isto é, usar o SQLAlchemy para definir uma tabela e as funções para criar o banco e salvar os dados. Aplicou-se a lógica de upsert, ou seja, se a criptomoeda já existe no banco, seus dados são atualizados, mas, caso ela não exista, é inserida. Seu script se chama manipulacao_banco_dados.py.

## Quarto passo - Disponibilização:

O script main.py inicializa o banco de dados, chama o cliente da API para buscar os dados e, na sequência, utiliza o manipulador do banco de dados para salvá-los, ou seja, ele orquestra todos os outros scripts.

## Quinto passo - Dashboard:

Foi confeccionado, utilizando o Power BI Desktop, um dashboard simples, apenas para mostrar, de uma forma mais prática e visual, os dados coletados.

## Como Executar o programa localmente:

### Pré-requisitos

- Python 3.8 ou superior
- Git (opcional, para clonar o repositório)

### 1. Preparação do Ambiente

Clone o repositório (ou simplesmente crie a estrutura de arquivos localmente):
git clone https://github.com/jaimemodestojr/desafiotecnicocadastra.git

Crie e ative um ambiente virtual:
Para o Windows:
python -m venv venv
.\venv\Scripts\activate

Instale todas as bibliotecas necessárias:
pip install -r requirements.txt

Configure sua API no site da Coin Cap e insira ela no arquivo config.py.

Com tudo configurado, execute o script principal:
python main.py

Ao final, será criado um arquivo chamado "CRIPTOMOEDAS.db", contendo os dados da API, extraídos e tratados.
