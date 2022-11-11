from flask import Blueprint

views = Blueprint("views", __name__)


def get_data(list_data, offset, per_page):
    return list_data[offset: offset + per_page]
