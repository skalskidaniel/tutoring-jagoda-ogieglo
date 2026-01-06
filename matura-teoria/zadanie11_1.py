
T = [None]

def d(x,n):
    n = n + 1
    T[n] = x # dodajemy element
    s = n
    while ((s // 2) >= 1) and (T[s] > T[s // 2]):
        pom = T[s]
        T[s] = T[s // 2]
        T[s // 2] = pom
        s = s // 2

T_do_przetestowania = [
    [26, 3, 5, -4],
    [36, 15, 17, 3],
    [27, 6, 13, 4, -3, -2, -3]
]

x_do_przetestowania = [
    5, -5, 30
]

for T_aktualne, x in zip(T_do_przetestowania, x_do_przetestowania):
    T = [None] + T_aktualne.copy() + [None]
    n = len(T_aktualne)
    d(x, n)
    print(f"Po wykonaniu funkcji {T=}")