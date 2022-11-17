

# Projeto proposto como desafio técnico. 

Um site feito em Python (linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte), Flask (microframework web escrito em Python), FastApi (framework web focado no desenvolvimento de APIs com Python), MongoDB (programa de banco de dados NoSQL), PyMongo (módulo Python que pode ser usado para interagir entre o banco de dados mongo e os aplicativos Python) e ElasticSearch (mecanismo de pesquisa).
## Apresentação

## O desafio proposto se divide em duas etapas:
### 1.º Etapa 
 
Utilizar as bases governamentais da receita federal que estão disponíveis neste link https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj que consiste em baixar as bases “Dados Abertos CNPJ EMPRESA”, “Dados Abertos CNPJ ESTABELECIMENTOS” e “Dados Abertos CNPJ SÓCIOS”, existem arquivos complementares que podem ser utilizados para colocar as legendas e esse outro link é a legenda de campos de cada arquivos https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/arquivos/leiaute-dos-arquivos.pdf 
 
Para efetuar o processamento a ideia é utilizar python puro e suas ferramentas nativas para processar com exceção do PyMongo que deverá ser utilizado como Banco de Processamento e Data Warehouse. Esse processamento precisa estar disponível em seu MongoDB e no seu ElasticSearch. 
 
Quantidade de CNPJs que precisam conter em sua base de dados que foram extraídos e processados é de 100.000 Registros. 
 
### 2.º Etapa 
 
O Segundo desafio consiste em criar uma aplicação simples em Python e Flask para o cliente efetuar o login e consultar esses dados pelos seguintes filtros, “CNPJ”, “Razão Social”, “Endereços” e “Telefones”. 
 
Como base de dados deverá ser utilizado o MongoDB para guardar os dados de login e cadastro e juntamente um registro de pesquisas feitas no sistema e os dados destas pesquisas devem vir do ElasticSearch. 

## Objetivos

- Exercitar os conhecimentos iniciais obtidos na Trybe no módulo de ciência da computação no que se refere a linguagem python; 
- Treinar a interpretação e utilização de novas stacks derivadas da modelagem de projetos de terceiros e consecutivamente a conceituação de suas sintaxes;
- Realizar pesquisas imersivas nas documentações das skills requeridas e supracitadas com objetivo de resolver as adversidades encontradas no desenvolvimento;
- Aplicar e praticar a habilidade de análise e/ou leitura de código;
- Observar características e comportamentos dos frameworks das novas stacks para identificar quais deles divergem e/ou convergem para com os comportamentos e caracteristicas das minhas linguagens de programação primárias (JavaScript e TypeScript);
- Aplicar os conhecimentos do banco de dados não relacional MongoDB;  


## Como usar
1. Clone o repositório

  - Use o comando: `git clone git@github.com:Italo9/teste-target-data.git`
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd teste-target-data`

### Com docker:
-  (EM CONSTRUÇÃO)
### Sem docker:
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  
 
## Melhorias Futuras

Aqui são apresentadas possíveis melhorias que ainda não foram implementadas no projeto.

- Utilizar variáveis de ambiente em sua totalidade; 
- Implementar testes unitários/integração;
- Implementar testes E2E;
- Aprimorar a estruturação do back end;
- Aplicar conceitos SOLID na apliação;
- Implementar ao Readme por meio de linguagem não verbal um gif da aplicação; 

## Referências Utilizadas

Além da documentação das técnologias previamente cidatas, também foram utilizados guias de implementação e projetos do gitHub. Abaixo são listadas as referências utilizadas:

- [Developing and Testing an Asynchronous API with FastAPI and Pytest](https://testdriven.io/blog/fastapi-crud/#get-routes)
- [Building a CRUD App with FastAPI and MongoDB](https://testdriven.io/blog/fastapi-mongo/#update)
- [The Ultimate FastAPI Tutorial](https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-1-hello-world/)
- [Github](https://github.com/rafamaga)
- [Flask Tutorial #5 - Sessions](https://www.youtube.com/watch?v=iIhAfX4iek0&t=376s)
