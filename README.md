

# Projeto proposto como desafio técnico 

O requerido projeto trata-se de um site feito em flask utilizando o Elasticsearch, como mecanismo de pesquisa (derivado da biblioteca Lucene), MongoDB como banco de dados não relacional, utilizando dados abertos da receita federal. Concerne em uma modelagem organizada em tabelas que expões informaçoes de empresas, estabelecimento e seus respectivos sócios.

# Pré-requisitos 

- [Python](https://docs.python.org/3/) (linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte);
- [Flask](https://flask.palletsprojects.com/en/2.2.x/) (microframework web escrito em Python);
- [MongoDB](https://www.mongodb.com/docs/) (programa de banco de dados NoSQL);
- [PyMongo](https://pymongo.readthedocs.io/en/stable/) (módulo Python que pode ser usado para interagir entre o banco de dados mongo e os aplicativos Python);
- [ElasticSearch](https://www.elastic.co/guide/index.html) (mecanismo de pesquisa).

## Apresentação

## O desafio proposto se divide em duas etapas:
### 1.º Etapa 
 
- Utilizar as bases governamentais da receita federal que estão disponíveis neste [link](https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj) que consiste em baixar as bases “Dados Abertos CNPJ EMPRESA”, “Dados Abertos CNPJ ESTABELECIMENTOS” e “Dados Abertos CNPJ SÓCIOS”, existem arquivos complementares que podem ser utilizados para colocar as legendas e esse outro [link](https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/arquivos/leiaute-dos-arquivos.pdf) é a legenda de campos de cada arquivos  
 
- Para efetuar o processamento a ideia é utilizar python puro e suas ferramentas nativas para processar com exceção do PyMongo que deverá ser utilizado como Banco de Processamento e Data Warehouse. Esse processamento precisa estar disponível em seu MongoDB e no seu ElasticSearch. 
 
- Quantidade de CNPJs que precisam conter em sua base de dados que foram extraídos e processados é de 100.000 Registros. 
 
### 2.º Etapa 
 
- O Segundo desafio consiste em criar uma aplicação simples em Python e Flask para o cliente efetuar o login e consultar esses dados pelos seguintes filtros, “CNPJ”, “Razão Social”, “Endereços” e “Telefones”. 
 
- Como base de dados deverá ser utilizado o MongoDB para guardar os dados de login e cadastro e juntamente um registro de pesquisas feitas no sistema e os dados destas pesquisas devem vir do ElasticSearch. 

## Objetivos

- Realizar pesquisas imersivas nas documentações das skills requeridas e supracitadas com objetivo de resolver as adversidades encontradas no desenvolvimento;
- Aplicar e praticar a habilidade de análise e/ou leitura de código;
- Observar características e comportamentos dos frameworks das novas stacks para identificar quais deles divergem e/ou convergem para com os comportamentos e caracteristicas das minhas linguagens de programação primárias (JavaScript e TypeScript);
- Aplicar os conhecimentos do banco de dados não relacional MongoDB;
- Realizar a manipulação de arquivos;
- Exercitar os conhecimentos iniciais obtidos na Trybe no módulo de ciência da computação no que se refere a linguagem python; 
- Treinar a interpretação e utilização de novas stacks derivadas da modelagem de projetos de terceiros e consecutivamente a conceituação de suas sintaxes;


## Como usar
 1. **Clonar o repositório**
  
  - Use o comando:
  ```bash
  git clone git@github.com:Italo9/teste-target-data.git
  ```
  - Entre na pasta do repositório que você acabou de clonar:
    ```bash
    cd teste-target-data
    ```
 2. **Baixar os três arquivos .csv e colocá-los no caminho `target/extrair_dados`** [baixar aqui](https://drive.google.com/drive/folders/1gNR9gBZD91umXB1RPJfs9i7VurAJcYwU?usp=share_link)

 3. **Criar o ambiente virtual**

  ```bash
  python3 -m venv .venv
  ```
 4. **Ativar o ambiente virtual**

  ```bash
  source .venv/bin/activate
  ```

 5. **Instalar as dependências no ambiente virtual**

  ```bash
  python3 -m pip install -r dev-requirements.txt
  ```

 Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
 Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.
 
 **Você utilizará o MongoDB Community Edition, escolha a instalação especifica para a sua distribuição Linux deste [link](https://www.mongodb.com/docs/manual/administration/install-on-linux/).**
 
 **Caso você esteja utilizando MacOS, siga as instruções deste [link](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/).**
 
 **Ou ainda, no Windows, siga as instruções deste [link](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/).**

 6. **Usar o comando na raiz do projeto para criar o banco e a coleção junto com os documentos inseridos**
 ```bash
 python3 target/extrair_dados/extrair_dados_csv.py
  ```
 7. **Usar o comando na raiz do projeto para criar a conexão com o elastic search**
 ```bash
 python3 target/elastic_search/conexao_elastic_search.py 
  ```
 8. **Usar o comando na raiz do projeto para executar a aplicação**
 ```bash
  python3 target/aplicacao/aplicacao.py
   ```
  - Acesse http://127.0.0.1:5000
  
### Com docker: (EM CONSTRUÇÃO)
  ```bash
  docker-compose up -d 
   ``` 
 
## Melhorias Futuras

Aqui são apresentadas possíveis melhorias que ainda não foram implementadas no projeto.

- Utilizar variáveis de ambiente em sua totalidade; 
- Implementar testes unitários/integração;
- Implementar testes E2E;
- Aprimorar a estruturação do back end;
- Aplicar conceitos SOLID na apliação;
- Reestruturar a aplicação para que a mesma seja executada via comando no terminal;
- Melhorar a didática e apresentação das informações do Readme adicionando, por exemplo, material não textual;
- Retificar estrutura para exercer vigência e conformidade com a arquitetura dinsponível no tutorial do [flask](https://flask.palletsprojects.com/en/2.2.x/tutorial/)  

## Referências Utilizadas

Além da documentação das técnologias previamente cidatas, também foram utilizados guias de implementação e projetos do gitHub. Abaixo são listadas as referências utilizadas:

- [Developing and Testing an Asynchronous API with FastAPI and Pytest](https://testdriven.io/blog/fastapi-crud/#get-routes)
- [Building a CRUD App with FastAPI and MongoDB](https://testdriven.io/blog/fastapi-mongo/#update)
- [The Ultimate FastAPI Tutorial](https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-1-hello-world/)
- [Github](https://github.com/rafamaga)
- [Flask Tutorial #5 - Sessions](https://www.youtube.com/watch?v=iIhAfX4iek0&t=376s)
- [Full-Text Search with Auto Complete - Python Flask & ElasticSearch](https://www.youtube.com/watch?v=-KjE1JmFVNY)
