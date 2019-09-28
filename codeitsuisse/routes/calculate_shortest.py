def calculate_shortest(s1, s2):
    cost = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cost += 1

    return cost


# def find_shortest(s, str_list):
#     min_trans = 99999999999999
#     for i in range(len(str_list)):
#         trans = calculate_shortest(s, str_list[i])
#         if trans < min_trans:
#             min_trans = trans
#             min_str = str_list[i]

#     return (min_trans, min_str)