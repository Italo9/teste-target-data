import os
from pymongo import MongoClient
from elasticsearch import Elasticsearch


MONGO_URL = os.environ.get("mongodb://localhost:27017")
SECRET_KEY = os.environ.get("7799Reis")
ELASTIC_CLOUD_ID = os.environ.get(
    """My_deployment:dXMtY2VudHJhbDEuZ2NwLmNsb3Vk
LmVzLmlvJGJiY2E4ODdhNmU4MjQzY2E4ZTIzZTNmYzUwMjUzMzQ0JDllYzM2Mz
EyMmZkNTQ4NTA5M2E4NTY3NDk0ZDkxNGNm"""
)
ELASTIC_USERNAME = os.environ.get("elastic")
ELASTIC_PASSWORD = os.environ.get("wxdXoUF9SA8ns30bW9pxrBI8")

client = MongoClient(MONGO_URL)
db = client.Teste_Python

es = Elasticsearch(
    cloud_id="""My_deployment:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJGJiY2E4ODdhNmU4MjQzY2E4ZTIz
    ZTNmYzUwMjUzMzQ0JDllYzM2MzEyMmZkNTQ4NTA5M2E4NTY3NDk0ZDkxNGNm""",
    basic_auth=("elastic", "wxdXoUF9SA8ns30bW9pxrBI8"),
)
