def szyfrowanie(tekst: str, klucz):
    zaszyfrowane = ""
    klucz %= 26
    for znak in tekst:
        if znak.isalpha():
            # jesli jest to literka
            granica = 122 if znak.islower() else 90
            na_ascii = ord(znak) + klucz
            if na_ascii > granica:
                na_ascii -= 26
            zaszyfrowane += chr(na_ascii)
        else:
            # jesli to nie jest literka
            zaszyfrowane += znak

    return zaszyfrowane

komenda, klucz = input().split()
klucz = int(klucz)

tekst = input().strip()

if komenda == "ODSZYFRUJ":
    print(szyfrowanie(tekst, -klucz))
elif komenda == "ZASZYFRUJ":
    print(szyfrowanie(tekst, klucz))
else:
    print("nieznana komenda")
