import logging
import json

from flask import request, jsonify, Blueprint;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

mod = Blueprint('square', __name__)

@mod.route('/square')
def evaluate():
    return "square evaluated!"
    # data = request.get_json();
    # logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input");
    # result = inputValue * inputValue
    # logging.info("My result :{}".format(result))
    # return json.dumps(result);



