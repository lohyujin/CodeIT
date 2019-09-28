import logging
import json

from flask import request, jsonify, Blueprint;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

mod = Blueprint('chessgame', __name__)

@mod.route('/chessgame', methods=['POST'])
def evaluate():
<<<<<<< HEAD
    data = request.get_json();
=======
    # return "chessgame evaluated!"
    data = request.get_json()
    print(type(data))
>>>>>>> 3958518c9e59430776e6231b1884191ffb6da9c8
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
<<<<<<< HEAD
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

=======
    if(k != ('','')):
        
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
>>>>>>> 3958518c9e59430776e6231b1884191ffb6da9c8
    logging.info("My result :{}".format(result))
    return json.dumps(result)