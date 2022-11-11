from elasticsearch import Elasticsearch
from pymongo import MongoClient
import os

MONGO_URL = os.environ.get("mongodb://localhost:27017")

client = MongoClient(MONGO_URL)
db = client.Teste_Python

es = Elasticsearch(
    cloud_id="""My_deployment:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJGJiY2E4ODdhNmU4MjQzY2E4ZTIz
    ZTNmYzUwMjUzMzQ0JDllYzM2MzEyMmZkNTQ4NTA5M2E4NTY3NDk0ZDkxNGNm""",
    http_auth=("elastic", "wxdXoUF9SA8ns30bW9pxrBI8"),
)

print(es.info())
