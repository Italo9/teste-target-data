from flask import (
    Blueprint,
    redirect,
    render_template,
    session,
    url_for,
    request,
    flash,
)
from settings import db
from werkzeug.security import check_password_hash

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


@user.route("/login", methods=["GET", "POST"])
def login():
    if "username" in session:
        return redirect(url_for("user.main"))
    elif request.method == "POST":
        username = request.form.get("user")
        password = request.form.get("password")
        if (username != "") and (password == ""):
            flash("Por favor, preencha todos os campos")
            return render_template(
                "views_users/login.html", type_alert="danger"
            )

        elif (username == "") and (password != ""):
            flash("Por favor, preencha todos os campos")
            return render_template(
                "views_users/login.html", type_alert="danger"
            )

        elif (username != "") and (password != ""):
            user_found = db.users.find_one({"name": username})
            if user_found:
                user_val = user_found["name"]
                passwordcheck = user_found["password"]
                if check_password_hash(passwordcheck, password):
                    session["username"] = user_val
                    return redirect(url_for("user.main"))
                else:
                    flash("Senha Incorreta", "error")
                    return render_template(
                        "views_users/login.html", type_alert="danger"
                    )
            else:
                flash("Usuário não encontrado")
                return render_template(
                    "views_users/login.html", type_alert="danger"
                )

        return redirect(url_for("user.pageCreate"))

    return render_template("views_users/login.html")
