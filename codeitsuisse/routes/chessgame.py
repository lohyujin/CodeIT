import logging
import json

from flask import request, jsonify, Blueprint;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

mod = Blueprint('chessgame', __name__)

@mod.route('/chessgame')
def evaluate():
    # return "chessgame evaluated!"
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("input");


    n = len(inputValue)

    x = []
    for i in range(len(inputValue)):
        row = inputValue[i]
        for j in range(len(row)):
            item = row[j]
            if item == 'K':
                k = (i, j)
            if item == 'X':
                x.append((i, j))

    result = 0
    i, j = k
    for a in range(0, j, -1):
        result += 1
        if (i, a) in x:
            break

    for a in range(j+1, n):
        result += 1
        if (i, a) in x:
            break

    
    for a in range(0, i, -1):
        result += 1
        if (a, j) in x:
            break

    for a in range(i+1, n):
        result += 1
        if (a, j) in x:
            break
    

    for a in range(min(i, j)):
        result += 1
        if (i-a, j-a) in x:
            break

    for a in range(min(i, n-j-1)):
        result += 1
        if (i-a, j+a) in x:
            break

    for a in range(min(n-i-1, j)):
        result += 1
        if (i+a, j-a) in x:
            break

    for a in range(min(n-i-1, n-j-1)):
        result += 1
        if (i+a, j+a) in x:
            break

    logging.info("My result :{}".format(result))
    return json.dumps(result);