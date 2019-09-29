import logging
import json
import random as rand

from flask import request, jsonify, Blueprint, Response

from codeitsuisse import app

logger = logging.getLogger(__name__)

lottery = Blueprint('lottery', __name__)

@lottery.route('/lottery', methods=['GET'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input")
    result = []
    for i in range (10):
        result.append(rand.randrange(30,80))

    logging.info("My result :{}".format(result))
    return Response(json.dumps(result), mimetype = 'application/json')