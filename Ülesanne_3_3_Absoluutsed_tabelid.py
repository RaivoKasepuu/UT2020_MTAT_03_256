"""
3.3 Absoluutsed tabelid
Tähtaeg: esmaspäev, 2. november 2020, 23.59
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö
Ülesanne on antud kahemõõtmelises arvude järjendis asendada kõik arvud nende absoluutväärtustega.

Kui arv on mittenegatiivne, siis selle absoluutväärtuseks nimetatakse arvu ennast. Kui arv on negatiivne, siis
absoluutväärtuseks on selle arvu vastandarv. Näiteks arvu 3 absoluutväärtus on 3 ja arvu -3 absoluutväärtus on 3.

Seda ülesannet tuleb lahendada kahel moel:

Kirjutada funktsioon absoluutne_tabel, mis võtab argumendiks kahemõõtmelise arvude järjendi ja tagastab uue
kahemõõtmelise järjendi, mis on saadud algsest nii, et kõik arvud on asendatud nende absoluutväärtustega.

Kirjutada funktsioon absolutiseeri_tabel, mis võtab argumendiks kahemõõtmelise arvude järjendi ja asendab selles
järjendis kõik arvud nende absoluutväärtustega. Funktsioon ei tagasta midagi.
Mõlemad funktsioonid lahendavad sama ülesannet, kuid oluline erinevus seisneb selles, et esimene tagastab uue tabeli,
vana muutmata, ning teine muudab olemasolevat tabelit, mitte midagi tagastamata.

Kontrollitakse vaid funktsioonide definitsioone, programmis neid rakendama ei pea.
"""

def absoluutne_tabel(matrix):
    result = []
    for i in range((len(matrix))):
        row=[]
        for j in range((len(matrix[i]))):
            row.append(abs(matrix[i][j]))
        result.append(row)
    return result


def absolutiseeri_tabel(matrix):
    for i in range((len(matrix))):
        for j in range((len(matrix[i]))):
            matrix[i][j] = abs(matrix[i][j])


tabel = [[1, -2], [-3, 4]]
print(absoluutne_tabel(tabel))

tabel = [[1, -2], [-3, 4]]
absolutiseeri_tabel(tabel)
print(tabel)
