from flask import Flask
import api.kalkulator
import api.user

app = Flask(__name__)

app.register_blueprint(api.kalkulator.routes)
app.register_blueprint(api.user.router)