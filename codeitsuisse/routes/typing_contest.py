import logging
import json

from calculate_shortest import calculate_shortest
from itertools import permutations

from flask import request, jsonify, Blueprint

from codeitsuisse import app

logger = logging.getLogger(__name__)

mod = Blueprint('typing-contest', __name__)

@mod.route('/typing-contest', methods=['POST'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    inputValue = data
    
    result = {}
    min_cost = float('inf')

    permutation_list = list(permutations(inputValue))
    for word_list in permutation_list:
        cost = 0
        steps = []
        for i in range(len(word_list)):
            if i == 0:
                steps.append({'type': 'INPUT', 'value': word_list[i]})
                cost += len(word_list[0])
            else:
                steps.append({'type': 'COPY', 'value': word_list[i-1]})
                cost += 1
                steps.append({'type': 'TRANSFORM', 'value': word_list[i]})
                cost += calculate_shortest(word_list[i-1], word_list[i])
        if cost < min_cost:
            min_cost = cost
            min_steps = steps

        result = {'cost': min_cost,
            'steps': min_steps}    

    logging.info("My result :{}".format(result))
    return jsonify(cost = min_cost, steps=min_steps)