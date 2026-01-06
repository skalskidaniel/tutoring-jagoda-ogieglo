def f(n):
    if n > 0:
        print(n, end=" ")
        f(n - 2)
        print(n, end=" ")

for liczba in [5, 6, 7, 8]:
    f(liczba)
    print()