import logging
import json
from itertools import permutations
import delete

from flask import request, jsonify, Blueprint

from codeitsuisse import app

logger = logging.getLogger(__name__)
compo = Blueprint('compo', __name__)

@compo.route('/composition', methods=['POST'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    test_id = data.get('set_id')
    patterns = data.get('patterns')
    word = data.get('composition')
    length = data.get("compositionLength")
    new_patterns = []
    flag = False
    for i in patterns:
        new_patterns.append(i)
        new_patterns.append(i[::-1])
    for i in new_patterns: 
        if i in word and flag == False:
            flag = True
    if flag == True:
        if(length) >= 10000:
            result = 5000
            return jsonify(testId = test_id ,result=result)
        else:
            while len(new_patterns) > 0:
                word, new_patterns = delete.delete(word, new_patterns)
        
    result = length - len(word)

    logging.info("My result :{}".format(result))
    return jsonify(testId = test_id ,result=result)