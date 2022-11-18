from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017")
print(client.list_database_names())

db = client.Teste_Python
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

limit = 100001

with open(
    "/home/italo/vaga-full-stack/teste-target-data/target/extrair_dados/empresas.csv",
) as db:
    for index, line in enumerate(db):
        data = {}
        line = line.replace(";", ",").replace("\n", "").replace('"', "")
        lista_line = line.split(",")

        for i in range(0, int(len(lista_empresas_keys))):
            value = lista_line[i]
            key = lista_empresas_keys[i]
            data[key] = value

        collection_empresas.insert_one(data)

        if index == limit:
            break

with open(
    "/home/italo/vaga-full-stack/teste-target-data/target/extrair_dados/socios.csv",
) as db:
    for index, line in enumerate(db):
        data = {}
        line = line.replace(";", ",").replace("\n", "").replace('"', "")
        lista_line = line.split(",")

        for i in range(0, int(len(lista_socios_keys))):
            value = lista_line[i]
            key = lista_socios_keys[i]
            data[key] = value

        collection_socios.insert_one(data)

        if index == limit:
            break

with open(
    "/home/italo/vaga-full-stack/teste-target-data/target/extrair_dados/estabele.csv",
) as db:
    for index, line in enumerate(db):
        data = {}
        line = line.replace(";", ",").replace("\n", "").replace('"', "")
        lista_line = line.split(",")

        for i in range(0, int(len(lista_estabelecimentos_keys))):
            value = lista_line[i]
            key = lista_estabelecimentos_keys[i]
            data[key] = value

        collection_estabelecimentos.insert_one(data)

        if index == limit:
            break
