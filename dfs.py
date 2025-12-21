# macierz sasiedztwa
# tabela = [[0 for _ in range(ilosc_kolumn)] for _ in range(ilosc_wierszy)]
# dodawanie połączenia
# tabela[wiersz][kolumna] = 1
# sprawdzanie połączenia
# tabela[<wierzcholek_poczatkowy>][<wierzchołek_docelowy>] .== 1

# [[], [], [], [], [], []]

# lista sąsiedztwa
# tabela = [[] for _ in range(ilosc_wierzcholkow)]
# dodawanie połączenia
# tabela[<wierzcholek_poczatkowy>].append(<wierzcholek_koncowy>)
# sprawdzanie połączenia
# tabela[<wierzchołek_początkowy>].count(<wierzcholek_docelowy>)
# LUB
# if <wierzcholek_docelowy> in tabela[<wierzchołek_początkowy>]


# stack = []
# dodaj do stosu
# stack.append()
# usun ze stosu
# stack.pop()
# sprawdzanie, czy jest pusty
# stack.is_empty()

# 3 4
# 0 1 <krawedz od 0 do 1>
# 0 2 <krawedz od 0 do 2>
# 1 3 <krawedz od 1 do 3>

# 3 krawedzie
# 4 wierzcholki
# tworzysz liste sasiedztwa z 4 wierzcholkamni
# for _ in range(3)
# dodaj krawedz
#

krawedzie, wierzcholki = list(map(int,input().split()))
lista_sasiedztwa = [[] for _ in range(wierzcholki)]
for _ in range(krawedzie):
    w1, w2 = list(map(int, input().split()))
    lista_sasiedztwa[w1].append(w2)
    lista_sasiedztwa[w2].append(w1)

for idx, sasiedzi in enumerate(lista_sasiedztwa):
    lista_sasiedztwa[idx] = sorted(sasiedzi, reverse=True)

def DFS(graf, start):
    g = graf.copy()
    odwiedzone = [False for _ in range(len(graf))]
    stos = []
    stos.append(start)
    while len(stos) != 0:
        v = stos.pop()
        if not odwiedzone[v]:
            odwiedzone[v] = True
            print(v)
            for s in lista_sasiedztwa[v]:
                if not odwiedzone[s]:
                    stos.append(s)


DFS(lista_sasiedztwa, 0)