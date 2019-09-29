import logging
import json

from toposort import toposort, toposort_flatten

from flask import request, jsonify, Blueprint

from codeitsuisse import app

logger = logging.getLogger(__name__)

generateSequence = Blueprint('generateSequence', __name__)

@generateSequence.route('/generateSequence', methods=['POST'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    input_modules = data.get('modules')
    input_dependency = data.get('dependencyPairs')

    dep = {}
    for pairs in input_dependency:
        dependee = pairs['dependee']
        dependentOn = pairs['dependentOn']
        if dependee in input_modules:
            if dependee not in dep:
                dep[dependee] = {dependentOn}
            else:
                dep[dependee].add(dependentOn)
    
    for module in input_modules:
        if module not in dep:
            dep[module] = {module}

    try:
        result = toposort_flatten(dep, sort=True)
    except ValueError as e:
        modules = input_modules.copy()
        for mod in e.data.keys():
            modules.remove(mod)
        result = getSequence({'modules': modules, 'dependencyPairs':input_dependency})

    logging.info("My result :{}".format(result))
    return json.dumps(result)