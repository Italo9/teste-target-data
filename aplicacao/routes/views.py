from flask import Blueprint, session, render_template
from flask_paginate import Pagination, get_page_args
from werkzeug.utils import redirect
from flask.helpers import url_for
from settings import (
    list_keys_empresas,
    list_all_dados_empresas,
    list_keys_socios,
    list_all_dados_socios,
)

views = Blueprint("views", __name__)


def get_data(list_data, offset, per_page):
    return list_data[offset: offset + per_page]


@views.route("/list-empresas")
def list_empresas():
    if "username" in session:
        page, per_page, offset = get_page_args(
            page_parameter="page", per_page_parameter="per_page"
        )
        keys_empresas = list_keys_empresas
        total = int(len(list_all_dados_empresas))
        pagination_empresas = get_data(
            list_all_dados_empresas, offset, per_page
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
        keys_socios = list_keys_socios
        total = int(len(list_all_dados_socios))
        pagination_socios = get_data(list_all_dados_socios, offset, per_page)
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
