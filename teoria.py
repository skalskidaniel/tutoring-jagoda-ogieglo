
def fun(a, b):
    if a <= 2:
        if a == 2:
            return True
        else:
            return False
    if a % b == 0:
        return False
    if b * b > a:
        return True
    licznik[0] += 1
    return fun(a, b +1)

for liczba in [2, 35, 17, 77]:
    licznik = [0]
    fun(liczba, 2)
    print(f"{liczba=} {licznik=}")
