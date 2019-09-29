import logging
import socket
from codeitsuisse import app
from codeitsuisse.routes.square import square
from codeitsuisse.routes.chessgame import mod
from codeitsuisse.routes.rpone import rpone
from codeitsuisse.routes.weddingnightmare import weddingnightmare
from codeitsuisse.routes.typing_contest import mod
from codeitsuisse.routes.portfolio import maximise
from codeitsuisse.routes.compo import compo
from codeitsuisse.routes.defuse import defuse
from codeitsuisse.routes.exponent import exponent
from codeitsuisse.routes.lottery import lottery
from codeitsuisse.routes.dependency import dependency
from codeitsuisse.routes.encrypt import encrypt

logger = logging.getLogger(__name__)

app.register_blueprint(square)
app.register_blueprint(mod)
app.register_blueprint(rpone)
app.register_blueprint(weddingnightmare)
app.register_blueprint(maximise)
app.register_blueprint(compo)
app.register_blueprint(defuse)
app.register_blueprint(exponent)
app.register_blueprint(lottery)
app.register_blueprint(dependency)
app.register_blueprint(encrypt)

@app.route('/')
def default_route():
    return "Python Template"


logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)



if __name__ == "__main__":
    logging.info("Starting application ...")
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.bind(('localhost', 5000))
    # port = sock.getsockname()[1]
    # sock.close()
    app.run(host='0.0.0.0', port=5000)
