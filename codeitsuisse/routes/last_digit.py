def last_digit(n1, n2):
    if n2 == 0:
        return 1

    cycle = [n1 % 10]
    while True:
        nxt = (cycle[-1] * n1) % 10
        if nxt == cycle[0]:
            break
        cycle.append(nxt)
    return cycle[(n2 - 1) % len(cycle)]