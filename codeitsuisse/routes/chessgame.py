import logging
import json

from flask import request, jsonify, Blueprint;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

mod = Blueprint('chessgame', __name__)

@mod.route('/chessgame', methods=['POST'])
def evaluate():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data

    print(inputValue)


    n = len(inputValue)

    x = []
    k = ('','')
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
    # horizontal
    for a in range(j-1, -1, -1):
        if (i, a) not in x:
            result += 1
        else:
            break

    for a in range(j+1, n):
        if (i,a) not in x:
            result += 1
        else:
            break

    # vertical
    for a in range(i-1, -1, -1):
        if (a, j) not in x:
            result += 1
        else:
            break

    for a in range(i+1, n):
        if (a, j) not in x:
            result += 1
        else:
            break
    
    # diagonal
    for a in range(min(i, j)):
        if (i-a, j-a) not in x:
            result += 1
        else:
            break

    for a in range(min(i, n-j-1)):
        if (i-a-1, j+a+1) not in x:
            result += 1
        else:
            break

    for a in range(min(n-i-1, j)):
        if (i+a+1, j-a-1) not in x:
            result += 1
        else:
            break

    for a in range(min(n-i-1, n-j-1)):
        if (i+a+1, j+a+1) not in x:
            result += 1
        else:
            break

    logging.info("My result :{}".format(result))
    return json.dumps(result)