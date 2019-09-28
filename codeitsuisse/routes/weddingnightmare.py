import logging
import json
import numpy as np

from flask import request, jsonify, Blueprint

from codeitsuisse import app

logger = logging.getLogger(__name__)

weddingnightmare = Blueprint('wedding-nightmare', __name__)

# [{
#   "test_case": 1,
#   "guests": 4,
#   "tables": 2,
#   "friends": [[2, 4]],
#   "enemies": [],
#   "families": []
# }, {
#   "test_case": 2,
#   "guests": 4,
#   "tables": 2,
#   "friends": [[2, 4]],
#   "enemies": [[2, 3], [1, 2]],
#   "families": []
# }]

# [
#   {
#     "test_case": 1,
#     "satisfiable": true,
#     "allocation": [[1,1], [2,1], [3,1], [4,1]]
#   }, {
#     "test_case": 2,
#     "satisfiable": false,
#     "allocation": []
#   }
# ]

@weddingnightmare.route('/wedding-nightmare', methods=['POST'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("input")

    test_case = 0
    satisfaction = True
    allocation = []

    dic = {     'test_case' : test_case,
                'satisfiable' : satisfaction,
                'allocation' : allocation,
            }
    result = []


    # loop tc
    for element in inputValue:
        table_count = element['tables']
        cur_table = 1

        # to np
        npfriend = np.array(element['friends'])
        npfam = np.array(element['families'])
        npenemy = np.array(element['enemies'])
        # flatten
        flatfriend = npfriend.flatten()
        flatfam = npfam.flatten()
        flatene = npenemy.flatten()
        # get unique
        friends = list(dict.fromkeys(flatfriend.tolist()))
        fams = list(dict.fromkeys(flatfam.tolist()))
    #     enemy = list(dict.fromkeys(flatene.tolist()))

    #     for pax in friends:
    #         if pax in flatene:
    #             test_case = element['test_case']
    #             satisfaction = False
    #             result.append(dic)
    #             break
    #         else:
    #             allocation.append([pax, table_count])
        
    #     [1,2,3,4]
        guest_list = list(range(1, element['guests']+1))
        
        while len(guest_list) > 0:
    #         for guest in guest_list:
        #         Loner
            if guest not in fams and guest not in friends:
                allocation.append([guest, cur_table])
            elif guest in fams:
    #                 find out who the fam is 
                result = np.where(npfam == guest)
                listOfCoordinates = list(zip(result[0], result[1]))
                toadd = list(dict.fromkeys(np.array(list(listOfCoordinates)).flatten().tolist()))
    #         coord = (1,3)
                for add in toadd:
                    allocation.append([add, cur_table])
                    guest_list.remove(add)

            
            guest_list.remove(guest)

    #     result.append(dic)


        logging.info("My result :{}".format(result))
        return json.dumps(result)