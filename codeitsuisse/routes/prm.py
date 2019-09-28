import logging
import json
from itertools import permutations

from flask import request, jsonify, Blueprint

from codeitsuisse import app

logger = logging.getLogger(__name__)
prm = Blueprint('prm', __name__)

@prm.route('/maximize_1a', methods=['POST'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    N = int(data.get("Starting Capital"))
    T = int(data.get("stocks"))
    
    logging.info("My result :{}".format(result))
    return jsonify(profit=,portfolio=result)