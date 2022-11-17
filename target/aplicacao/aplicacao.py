from flask import Flask
from routes.users import user

from routes.views import views

app = Flask(__name__)

config_object = "settings"
app.config.from_object(config_object)

app.register_blueprint(user)
app.register_blueprint(views)


if __name__ == "__main__":
    app.secret_key = "XABLAU"
    app.debug = True
    app.run()
