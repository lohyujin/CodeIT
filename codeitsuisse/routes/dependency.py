import logging
import json

from flask import request, jsonify, Blueprint
from collections import defaultdict, deque
from topology_sort import topological

from codeitsuisse import app

logger = logging.getLogger(__name__)

dependency = Blueprint('dependency', __name__)

@dependency.route('/generateSequence', methods=['POST'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    modules = data.get("modules")
    dependencyPairs = data.get("dependencyPairs")


    modules = data.get("modules")
    dependencyPairs = data.get("dependencyPairs")
    result = []

    # adjacent list
    adjacent_list = defaultdict()
    for item in dependencyPairs:
        # main = item[0]
        # sub = item[1]
        dependee = item['dependee']
        dependentOn = item['dependentOn']
        # existing mod
        if dependee in adjacent_list.keys():
            adjacent_list[dependee].append(dependentOn)
        else:
            adjacent_list[dependee] = [dependentOn]


    # no dependency
    for item in modules:
        if item not in adjacent_list.keys():
            adjacent_list[item] = ['']


    # visited list
    # visited_list = defaultdict()
    # for item in modules:
    #     visited_list[item] = False


    # for vertex in visited_list:
    #     topology_sort(adjacent_list, visited_list, output_stack, vertex)

    # print(output_stack)

    output = topological(adjacent_list)

    # no error
    if '' in output:
        if len(output)-1 == output.index(''):
            output = output[::-1]
            result = output[1:]
        else:
            for item in output:
                if item == '':
                    break
                result.append(item)
    else:
        result = output


    logging.info("My result :{}".format(result[1:]))
    return json.dumps(result[1:])