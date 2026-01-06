
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


# print(funkcja(10,"bbbbbbbbbb")) k = 10
print(funkcja(10,"ababababaa")) # k = 5


# aaaaabbbbb
# A = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
# B = [5, 5, 5, 5, 5, 5, 4, 3, 2, 1]
# k = 10

# ababababab
# A = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
# B = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
# k = 6

# ababababaa
# A = [1,1,2,2,3,3,4,4,5,5]
# B = [4,4,3,3,2,2,1,1,0,0]
# k = 5