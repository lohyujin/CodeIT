import logging
import json
import numpy as np
import itertools

from flask import request, jsonify, Blueprint


# from codeitsuisse import app

logger = logging.getLogger(__name__)

maximise = Blueprint('maximise', __name__)

@maximise.route('/maximise_1a', methods=['POST'])
def maximise_1a():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))


    result = { "profit": 0,
                "portfolio":[]
                }
    master = []

    capital = data.get("startingCapital")
    capitall = data.get("startingCapital")

    # 2d array
    stocks = data.get("stocks")

    # ---- Greedy algo start ----------
    # npstocks = np.array(stocks)
    # small = []
    # for i in stocks:
    #     small.append([i[1]/i[2]])

    # yields = np.array(small)
    # stocks = np.append(npstocks, yields, axis=1)
    # stocks[stocks[:,3].argsort()]
    # # print(stocks)

    # for stock in stocks.tolist()[::-1]:
    #     if capital > float(stock[2]):
    #         result['portfolio'].append(stock[0])
    #         result['profit'] += float(stock[1])
    #         capital -= float(stock[2])

    # master.append(result)

    # ------- end of greedy -----------

    # ------ start no remaining algo -----------

    mod = { "profit": 0,
                "portfolio":[]
                }

    for count in range(1,len(stocks)+1):
        cur = 0

        price = 0
        profit = 0
        port = []
        # loop n digits
        for combi in itertools.combinations(stocks, count):
            # for item in combi:
            #     # print(item)
            #     cur += item[1]

            #     port.append(item[0])
            # no remainder
            # if capital == cur:
            # print(combi)
            npcombi = np.array(list(combi))
            xponse = np.transpose(npcombi)

            port = xponse[0].tolist()
            # print(port)
            profit = sum(map(int, xponse[1].tolist()))
            cur = sum(map(int, xponse[2].tolist()))
            # print(cur)
            if capitall - cur > 10:
                mod['profit'] = profit
                mod['portfolio'] = port
                # print(port)
                master.append(mod)
                mod = { "profit": 0,
                        "portfolio":[]
                        }

    # ---------- end of no remaining algo -------

    answer = sorted(master, key = lambda i: i['profit'], reverse=True)

    logging.info("My result :{}".format(answer[0]))
    return json.dumps(answer[0])




@maximise.route('/maximise_1b', methods=['POST'])
def maximise_1a():
data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))


    result = { "profit": 0,
                "portfolio":[]
                }
    master = []

    capital = data.get("startingCapital")
    capitall = data.get("startingCapital")

    # 2d array
    stocks = data.get("stocks")

    # ---- Greedy algo start ----------
    npstocks = np.array(stocks)
    small = []
    for i in stocks:
        small.append([i[1]/i[2]])

    yields = np.array(small)
    stocks = np.append(npstocks, yields, axis=1)
    stocks[stocks[:,3].argsort()]
    # print(stocks)

    # buy all stocks
    for stock in stocks.tolist()[::-1]:
        if capital > float(stock[2]):
            result['portfolio'].append(stock[0])
            result['profit'] += float(stock[1])
            capital -= float(stock[2])


    # greedy yield
    for stock in stocks.tolist()[::-1]:
        if capital > float(stock[2]):
            # print('before ' + str(capital))
            while capital // float(stock[2]) >= 1:
                result['portfolio'].append(stock[0])
                result['profit'] += float(stock[1])
                capital -= float(stock[2])
                # print('after ' + str(capital))

    master.append(result)



    # ------- end of greedy -----------

    
    answer = sorted(master, key = lambda i: i['profit'], reverse=True)

    logging.info("My result :{}".format(answer[0]))
    return json.dumps(answer[0])