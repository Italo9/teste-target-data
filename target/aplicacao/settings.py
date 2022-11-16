import os
from pymongo import MongoClient
from elasticsearch import Elasticsearch


MONGO_URL = os.environ.get("MONGO_URI")
SECRET_KEY = os.environ.get("7499Reis")
ELASTIC_CLOUD_ID = os.environ.get("ELASTIC_CLOUD_ID")
ELASTIC_USERNAME = os.environ.get("ELASTIC_USERNAME")
ELASTIC_PASSWORD = os.environ.get("ELASTIC_PASSWORD")

client = MongoClient(MONGO_URL)
db = client.Teste_Python

es = Elasticsearch(
    cloud_id="""My_deployment:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJGJiY2E4ODdhNmU4MjQzY2E4ZTIz
    ZTNmYzUwMjUzMzQ0JDllYzM2MzEyMmZkNTQ4NTA5M2E4NTY3NDk0ZDkxNGNm""",
    basic_auth=("elastic", "wxdXoUF9SA8ns30bW9pxrBI8"),
)

collection_empresas = db.Empresas
collection_socios = db.Socios
collection_estabelecimentos = db.Estabelecimentos

lista_empresas_keys = [
    "CNPJ BÁSICO",
    "RAZÃO SOCIAL/NOME EMPRESARIAL",
    "NATUREZA JURÍDICA",
    "QUALIFICAÇÃO DO RESPONSÁVEL",
    "CAPITAL SOCIAL DA EMPRESA",
    "PORTE DA EMPRESA",
    "ENTE FEDERATIVO RESPONSÁVEL",
]

lista_socios_keys = [
    "CNPJ BÁSICO",
    "IDENTIFICADOR DE SÓCIO",
    "NOME DO SÓCIO (NO CASO PF) OU RAZÃO SOCIAL (NO CASO PJ)",
    "CNPJ/CPF DO SÓCIO",
    "QUALIFICAÇÃO DO SÓCIO",
    "DATA DE ENTRADA SOCIEDADE",
    "PAIS",
    "REPRESENTANTE LEGAL",
    "NOME DO REPRESENTANTE",
    "QUALIFICAÇÃO DO REPRESENTANTE LEGAL",
    "FAIXA ETÁRIA",
]

lista_estabelecimentos_keys = [
    "CNPJ BÁSICO",
    "CNPJ ORDEM",
    "CNPJ DV",
    "IDENTIFICADOR MATRIZ/FILIAL",
    "NOME FANTASIA",
    "SITUAÇÃO CADASTRAL",
    "DATA SITUAÇÃO CADASTRAL",
    "MOTIVO SITUAÇÃO CADASTRAL",
    "NOME DA CIDADE NO EXTERIOR",
    "PAIS",
    "DATA DE INICIO ATIVIDADE",
    "CNAE FISCAL PRINCIPAL",
    "CNAE FISCAL SECUNDÁRIA",
    "TIPO DE LOGADOURO",
    "LOGADOURO",
    "NÚMERO",
    "COMPLEMENTO",
    "BAIRRO",
    "CEP",
    "UF",
    "MUNICÍPIO",
    "DDD 1",
    "TELEFONE 1",
    "DDD 2",
    "TELEFONE 2",
    "DDD DO FAX",
    "FAX",
    "CORREIO ELETRÔNICO",
    "SITUAÇÃO ESPECIAL",
    "DATA DA SITUAÇÃO ESPECIAL",
]

lista_empresas = collection_empresas.find({})
lista_socios = collection_socios.find({})
lista_estabele = collection_estabelecimentos.find({})

lista_todos_os_dados_das_empresas = []
lista_todos_os_dados_dos_socios = []
lista_todos_os_dados_dos_estabele = []

for index in lista_empresas:
    del index["_id"]
    lista_todos_os_dados_das_empresas += [index]

for index in lista_socios:
    del index["_id"]
    lista_todos_os_dados_dos_socios += [index]

for index in lista_estabele:
    del index["_id"]
    lista_todos_os_dados_dos_estabele += [index]
