import logging
import json
import re
from loop import loop

from flask import request, jsonify, Blueprint

from codeitsuisse import app

logger = logging.getLogger(__name__)

encrypt = Blueprint('encrypt', __name__)

@encrypt.route('/encryption', methods=['POST'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    print(type(data))
    result = []

    for case in data:
        n = case['n']
        # cleaning text
        patterns = [r'\w+']
        for p in patterns:
            match = re.findall(p, case['text'])
            txt = ''.join(match)
            txt = txt.upper()

        # encrypting...
        answer = loop(txt, n)
        result.append(answer)

    logging.info("My result :{}".format(result))
    return json.dumps(result)