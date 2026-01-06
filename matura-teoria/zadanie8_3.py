
def funkcja(n, s: str):
    A = [None for _ in range(n+1)]
    B = [None for _ in range(n+2)]
    s = '%' + s # dodajemy cokolwiek z przodu aby indeksowanie bylo od 1
    A[0] = 0
    for i in range(1,n+1):
        if s[i] == "a":
            A[i] = A[i-1] + 1
        else:
            A[i] = A[i-1]
    B[n+1] = 0
    for j in range(n,0,-1):
        if s[j] == "b":
            B[j] = B[j+1] + 1
        else:
            B[j] = B[j+1]
    k = 1
    for i in range(0,n+1):
        if A[i] + B[i+1] > k:
            k = A[i] + B[i+1]
    return k


s = 'a' * 300 + "b" * 550 + 'a' * 300 + 'b' * 7 + 'a' * 280 + 'b' * 110

print(funkcja(300 + 550 + 300 + 7 + 280 + 110, s))