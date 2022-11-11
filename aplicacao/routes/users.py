from flask import (
    Blueprint,
    redirect,
    url_for,
    render_template,
    session,
)

user = Blueprint("user", __name__)


@user.route("/")
def index():
    return redirect(url_for("user.login"))


@user.route("/main")
def main():
    if "username" in session:
        return render_template("views_users/main.html")
    else:
        return redirect(url_for("user.index"))
