from flask import Flask;
app = Flask(__name__)
from codeitsuisse.routes import square


app.register_blueprint(square.mod)