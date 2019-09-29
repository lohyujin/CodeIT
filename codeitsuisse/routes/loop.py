def loop(txt, n):
    # 0 to len - 1
    # for i in range(len(txt)):
    # if i == 0:
    #     toreturn += txt[i]
    #     txt.replace(txt[i], '')
    #     print(txt)

    # stop condition
    if len(txt) < n:
        return txt
    toreturn = ''
    remaining = txt
    # jackpot - need to remove from txt
    for i in range(len(txt)):
        if i % n == 0:
            toreturn += txt[i]
            remaining = remaining.replace(txt[i], '', 1)
    
    return toreturn + loop(remaining, n)