from flask import Flask
import api.kalkulator
import api.user
import api.admin

app = Flask(__name__)

app.register_blueprint(api.kalkulator.routes)
app.register_blueprint(api.user.router)
app.register_blueprint(api.admin.router)