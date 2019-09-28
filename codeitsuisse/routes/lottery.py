import logging
import json

import random

from flask import request, jsonify, Blueprint

from codeitsuisse import app

logger = logging.getLogger(__name__)

lottery = Blueprint('lottery', __name__)

@lottery.route('/lottery', methods=['GET'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    result = []
    for i in range(10):
        result.append(randon.randint(0, 100))
    logging.info("My result :{}".format(result))
    return jsonify(['result': result])