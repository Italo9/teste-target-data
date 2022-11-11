from flask import Flask
from routes.users import user

# from routes.views import views

app = Flask(__name__)
config_object = "settings"
app.config.from_object(config_object)

app.register_blueprint(user)
# app.register_blueprint(views)
app.run()
