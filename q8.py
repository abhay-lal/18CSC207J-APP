for i in range(100, 401):
    i = str(i)
    c = len(i)
    d = 0
    for j in i:
        j = int(j)
        if j % 2 == 0:
            d += 1
    if c == d:
        print(i, end=",")