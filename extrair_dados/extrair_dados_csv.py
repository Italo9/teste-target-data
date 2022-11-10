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
