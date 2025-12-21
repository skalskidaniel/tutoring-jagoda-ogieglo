
def sito(poczatek, koniec):
    L = [True for _ in range(koniec + 1)]
    L[0] = False
    L[1] = False

    for idx in range(2, koniec + 1):
        if L[idx]:
            for idx2 in range(2 * idx, koniec + 1, idx):
                L[idx2] = False

    Lp = []
    for i in range(poczatek, koniec + 1):
        if L[i]:
            Lp.append(i)
    return Lp

poczatek, koniec = map(int, input().split())
print(str(sito(poczatek, koniec))[1:-1])

# s = map(str, sito(poczatek, koniec))
# print(", ".join(s))

