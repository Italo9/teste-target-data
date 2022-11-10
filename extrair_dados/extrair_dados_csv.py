from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
print(client.list_database_names())

db = client.Teste_Python
collection_empresas = db.Empresas
collection_socios = db.Socios
collection_estabelecimentos = db.Estabelecimentos
