A = []
licznik = [0]
def f(p,q):
    if p != q:
        k = (q-p+1) // 2
        for i in range(1, k + 1):
            licznik[0] += 1
            A[p+i-1], A[q-k+i] = A[q-k+i], A[p+i-1]
        f(p, p+k -1)
        f(q - k + 1, q)


# do_przetestowania = [[2,3,4], [1,2,3,4], list(range(1, 11))]
# for opcja in do_przetestowania:
#     licznik = [0]
#     A = opcja.copy()
#     f(1, len(A))
#     print(f"{opcja=}\nwynik: {A=}")

do_przetestowania = [4, 8, 16, 256]
for n in do_przetestowania:
    A = list(range(n))
    licznik = [0]
    f(1, n)
    print(f"{n = } {licznik[0] = }")