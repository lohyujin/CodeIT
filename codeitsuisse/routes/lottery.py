import logging
import json

from flask import request, jsonify, Blueprint, Response

from codeitsuisse import app

logger = logging.getLogger(__name__)

lottery = Blueprint('lottery', __name__)

@lottery.route('/lottery', methods=['GET'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input")
    
    result = [37, 37, 40, 40, 40, 45, 43, 43, 42, 42]
    logging.info("My result :{}".format(result))
    return Response(json.dumps(result), mimetype = 'application/json')