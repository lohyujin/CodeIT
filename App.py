import logging
import socket
from codeitsuisse import app
from codeitsuisse.routes.square import square
logger = logging.getLogger(__name__)

app.register_blueprint(square)

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
