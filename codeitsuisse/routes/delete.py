def delete(word, b):
    c = list(word)
    proxy = list(b)
    # print(proxy)
    letter = ''
    count = 0
    for i in c:
        counter = 0
        d = list(word)
        d.remove(i)
        new_word = ''.join(d)
        for pair in b:
            if pair not in new_word:
                counter += 1
        if counter >= count:
            count = counter
            letter = i
    c.remove(letter)
    remaining = ''.join(c)
    for pair in proxy:
        if pair not in remaining:
            b.remove(pair)
    # print(remaining)
    # print(b)
    return remaining,b