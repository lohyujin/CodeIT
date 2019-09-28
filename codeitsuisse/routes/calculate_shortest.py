def calculate_shortest(s1, s2):
    cost = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cost += 1

    return cost