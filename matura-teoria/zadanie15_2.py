def funkcja(n):
    w = 0
    while n != 0:
        w = w + (n% 10)
        # print(w)
        n //= 10
    return w

print(funkcja(11111))