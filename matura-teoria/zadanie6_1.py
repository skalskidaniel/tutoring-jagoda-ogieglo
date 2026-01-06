def f(x):
    i = 2
    while x % i != 0:
        i = i+1
    return x

def g(x):
    i = x - 1
    while x % i != 0:
        i = i-1
    return i

# 1.
# print(f"{f(2)=}")
# print(f"{g(2)=}")

# 2.
# for liczba in range(2, 10**6, 2):
#     if f(liczba) % 2 == 1:
#         print("NIE KAŻDA")
#         break

# 3.
# for liczba in range(2, 10**6, 2):
#     if g(liczba) % 2 == 1:
#         print("NIE KAŻDA")
#         break

# 4.

for x in range(3, 100):
    if x % f(x) != 0:
        print("nie")
        break