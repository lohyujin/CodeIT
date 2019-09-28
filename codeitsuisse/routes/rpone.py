import logging
import json
from itertools import permutations

from flask import request, jsonify, Blueprint

from codeitsuisse import app

logger = logging.getLogger(__name__)

rpone = Blueprint('rpone', __name__)

@rpone.route('/readyplayerone', methods=['POST'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    i = 1
    N = data.get("maxChoosableInteger")
    T = data.get("desiredTotal")
    a = []
    jar1 = list(range(1, N+1))
    while i < len(jar1):
        perms = permutations(jar1, i)   
        for perm in list(perms):
            if (sum(perm) >= T and len(perm) % 2 == 1):
                a.append(perm)
    i = i + 1
    sorted(a, key=len)
    if(len(a) > 0):
        result = len(a[0])
    else:
        result = -1
    logging.info("My result :{}".format(result))
    return jsonify(['result': result])