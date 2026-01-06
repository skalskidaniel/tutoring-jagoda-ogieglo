
T = [None, None]

def d(x,n):
    n = n + 1
    T[n] = x # dodajemy element
    s = n
    while ((s // 2) >= 1) and (T[s] > T[s // 2]):
        pom = T[s]
        T[s] = T[s // 2]
        T[s // 2] = pom
        s = s // 2


do_dodania = [6, -4, 12, 27, 26, 8]
for x in do_dodania:
    n = len(T) - 2
    d(x, n)

print(T)