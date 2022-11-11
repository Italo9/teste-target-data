from elasticsearch import Elasticsearch
from pymongo import MongoClient
import os

MONGO_URL = os.environ.get("mongodb://localhost:27017")

client = MongoClient(MONGO_URL)
db = client.Teste_Python

es = Elasticsearch(
    cloud_id="""My_deployment:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJGJiY2E4ODdhNmU4MjQzY2E4ZTIz
    ZTNmYzUwMjUzMzQ0JDllYzM2MzEyMmZkNTQ4NTA5M2E4NTY3NDk0ZDkxNGNm""",
    basic_auth=("elastic", "wxdXoUF9SA8ns30bW9pxrBI8"),
)

print(es.info())

collection_empresas = db.Empresas
collection_socios = db.Socios
collection_estabelecimentos = db.Estabelecimentos

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

for i, data in enumerate(lista_todos_os_dados_das_empresas):
    result = es.index(index="empresas", id=i + 1, document=data)
print("Status da inserção:", result)

for i, data in enumerate(lista_todos_os_dados_dos_socios):
    result = es.index(index="socios", id=i + 1, document=data)
print("Status da inserção:", result)

for i, data in enumerate(lista_todos_os_dados_dos_estabele):
    result = es.index(index="estabelecimentos", id=i + 1, document=data)
print("Status da inserção:", result)
