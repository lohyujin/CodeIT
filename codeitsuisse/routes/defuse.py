import logging
import json

from flask import request, jsonify, Blueprint

from codeitsuisse import app

logger = logging.getLogger(__name__)

defuse = Blueprint('defuse', __name__)

@defuse.route('/defuse', methods=['POST'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    result = []
    for row in data:
        n = row.get('n')
        k = row.get('k')
        password = row.get('password')

        total = 0

        if n >= 3:
            for sub in range(3, n+1, 2):
                for i in range(n-sub+1):
                    sub_array = password[i:i+sub]
                    if sub_array == sub_array[::-1]:
                        num_rand = sub_array.count(-1)
                        if num_rand % 2 == 0:
                            num = num_rand // 2
                        else:
                            num = num_rand // 2 + 1

                        total += k ** num 
    
        total = total % 998244353
        result.append(total)

    logging.info("My result :{}".format(result))
    return jsonify(result=result)