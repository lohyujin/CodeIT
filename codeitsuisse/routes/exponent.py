import logging
import json
from itertools import permutations
import math
from last_digit import last_digit

from flask import request, jsonify, Blueprint

from codeitsuisse import app

logger = logging.getLogger(__name__)
exponent = Blueprint('exponent', __name__)

@exponent.route('/exponent', methods=['POST'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    n = int(data.get("n"))
    p = int(data.get("p"))
    if(n < 0):
        n = n * -1
    elif(n == 0):
        result = [0,1,0]
        return jsonify(result=result)
    print(p)
    digits = p * math.log10(n)
    remainder1 = digits % 1
    print(remainder1)
    remainder2 = remainder1 % 1
    first = 10 ** remainder2
    first_digit = first // 1
    last_dig = last_digit(n,p)
    digits = digits + 1

    result = [int(first_digit), int(digits), int(last_dig)]
    logging.info("My result :{}".format(result))
    return jsonify(result=result)

