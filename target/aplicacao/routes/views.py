from datetime import date, datetime
from flask import Blueprint, session, render_template, request, flash
from flask.helpers import url_for
from werkzeug.utils import redirect
from settings import (
    lista_empresas_keys,
    lista_todos_os_dados_das_empresas,
    lista_socios_keys,
    lista_todos_os_dados_dos_socios,
    lista_estabelecimentos_keys,
    lista_todos_os_dados_dos_estabele,
    es,
    db,
)

from flask_paginate import Pagination, get_page_args

views = Blueprint("views", __name__)


def get_data(list_data, offset, per_page):
    return list_data[offset: offset + per_page]


@views.route("/list-empresas")
def list_empresas():
    if "username" in session:
        page, per_page, offset = get_page_args(
            page_parameter="page", per_page_parameter="per_page"
        )
        keys_empresas = lista_empresas_keys
        total = int(len(lista_todos_os_dados_das_empresas))
        pagination_empresas = get_data(
            lista_todos_os_dados_das_empresas, offset, per_page
        )
        pagination = Pagination(
            page=page, per_page=per_page, total=total, record_name="empresas"
        )
        return render_template(
            "views/list_empresas.html",
            head=keys_empresas,
            title="Dados Empresas",
            dados=pagination_empresas,
            pagination=pagination,
        )
    else:
        return redirect(url_for("user.login"))


@views.route("/list-socios")
def list_socios():
    if "username" in session:
        page, per_page, offset = get_page_args(
            page_parameter="page", per_page_parameter="per_page"
        )
        keys_socios = lista_socios_keys
        total = int(len(lista_todos_os_dados_dos_socios))
        pagination_socios = get_data(
            lista_todos_os_dados_dos_socios, offset, per_page
        )
        pagination = Pagination(
            page=page, per_page=per_page, total=total, record_name="socios"
        )
        return render_template(
            "views/list_socios.html",
            head=keys_socios,
            title="Dados Sócios",
            dados=pagination_socios,
            pagination=pagination,
        )
    else:
        return redirect(url_for("user.login"))


@views.route("/list-estabelecimentos")
def list_estabelecimentos():
    if "username" in session:
        page, per_page, offset = get_page_args(
            page_parameter="page", per_page_parameter="per_page"
        )
        keys_estabelecimentos = lista_estabelecimentos_keys
        total = int(len(lista_todos_os_dados_dos_estabele))
        pagination_estabelecimentos = get_data(
            lista_todos_os_dados_dos_estabele, offset, per_page
        )
        pagination = Pagination(
            page=page,
            per_page=per_page,
            total=total,
            record_name="estabelecimentos",
        )
        return render_template(
            "views/list_estabelecimentos.html",
            head=keys_estabelecimentos,
            title="Dados Estabelecimentos",
            dados=pagination_estabelecimentos,
            pagination=pagination,
        )
    else:
        return redirect(url_for("user.login"))


@views.route("/search", methods=["GET", "POST"])
def search():

    if "username" in session:

        query = request.form.get("search")

        data_now = datetime.now()
        data_str = str(date.today())
        hora_str = data_now.strftime("%H:%M:%S")

        data_search = {"word": query, "date": data_str, "hour": hora_str}

        collection_log = db.logs

        log_found = collection_log.find_one({"id": 1})

        if log_found:

            collection_log.update_one(
                {"id": 1}, {"$push": {"logs": data_search}}
            )
        else:
            list_data_search = [data_search]

            document = {"id": 1, "logs": list_data_search}

            collection_log.insert_one(document)

        dados_empresas = es.search(
            index="empresas",
            body={
                "query": {
                    "multi_match": {
                        "query": query,
                        "type": "phrase",
                        "fields": [
                            "CNPJ BÁSICO",
                            "RAZÃO SOCIAL/NOME EMPRESARIAL",
                        ],
                    }
                }
            },
        )

        dados_socios = es.search(
            index="socios",
            body={
                "query": {
                    "multi_match": {
                        "query": query,
                        "type": "phrase",
                        "fields": [
                            "CNPJ BÁSICO",
                            """NOME DO SÓCIO (NO CASO PF) OU RAZÃO SOCIAL
                            (NO CASO PJ)""",
                        ],
                    }
                }
            },
        )

        dados_estabelecimentos = es.search(
            index="estabelecimentos",
            body={
                "query": {
                    "multi_match": {
                        "query": query,
                        "type": "phrase",
                        "fields": [
                            "CNPJ BÁSICO",
                            "PAIS",
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
                        ],
                    }
                }
            },
        )

        list_empresas = []
        list_socios = []
        list_estabelecimentos = []

        if dados_empresas["hits"]["hits"] != []:

            for i in dados_empresas["hits"]["hits"]:
                list_empresas.append(i["_source"])
            title_empresas = "Dados Empresas"
            keys_empresas = lista_empresas_keys
        else:

            title_empresas = ""
            keys_empresas = ""

        if dados_socios["hits"]["hits"] != []:
            for i in dados_socios["hits"]["hits"]:
                list_socios.append(i["_source"])
            title_socios = "Dados Sócios"
            keys_socios = lista_socios_keys
        else:
            title_socios = ""
            keys_socios = ""

        if dados_estabelecimentos["hits"]["hits"] != []:
            for i in dados_estabelecimentos["hits"]["hits"]:
                list_estabelecimentos.append(i["_source"])
            title_estabelecimentos = "Dados Estabelecimentos"
            keys_estabelecimentos = lista_estabelecimentos_keys
        else:
            title_estabelecimentos = ""
            keys_estabelecimentos = ""
        qtd_hits = (
            len(list_empresas) + len(list_socios) + len(list_estabelecimentos)
        )
        if (
            (list_empresas == [])
            and (list_socios == [])
            and (list_estabelecimentos == [])
        ):
            flash("Infelizmente não encontramos nenhum registro na sua busca")
            return render_template("views/none.html")
        else:
            flash(f"Foi encontrado {qtd_hits} itens na sua busca")
            return render_template(
                "views/list.html",
                dados_empresas=list_empresas,
                head_empresas=keys_empresas,
                title_empresas=title_empresas,
                dados_socios=list_socios,
                head_socios=keys_socios,
                title_socios=title_socios,
                dados_estabelecimentos=list_estabelecimentos,
                head_estabelecimentos=keys_estabelecimentos,
                title_estabelecimentos=title_estabelecimentos,
            )
    else:
        return redirect(url_for("user.login"))
