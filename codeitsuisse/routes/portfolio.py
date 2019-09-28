import logging
import json
import numpy as np

from flask import request, jsonify, Blueprint


# from codeitsuisse import app

logger = logging.getLogger(__name__)

maximise = Blueprint('maximise_1a', __name__)


@maximise.route('/maximise_1a', methods=['POST'])
def maximise_1a():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("startingCapital")

        
    result = { "profit": 0,
                "portfolio":[]
                }

    capital = data.get("startingCapital")
    # 2d array
    stocks = data.get("stocks")
    npstocks = np.array(stocks)
    small = []
    for i in stocks:
        small.append([i[1]/i[2]])

    yields = np.array(small)
    stocks = np.append(npstocks, yields, axis=1)
    stocks[stocks[:,3].argsort()]
    print(stocks)

    for stock in stocks.tolist()[::-1]:
        if capital > float(stock[2]):
            result['portfolio'].append(stock[0])
            result['profit'] += float(stock[1])
            capital -= float(stock[2])




    logging.info("My result :{}".format(result))
    return json.dumps(result)