from flask import (
    Blueprint,
    redirect,
    url_for,
)

user = Blueprint("user", __name__)


@user.route("/")
def index():
    return redirect(url_for("user.login"))
