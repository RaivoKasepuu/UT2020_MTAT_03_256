"""
1.2 Reeglite kontrollimine
Tähtaeg: esmaspäev, 5. oktoober 2020, 23.59
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö

Koostada funktsioon on_bingo_tabel, mis võtab argumendiks 5 x 5 maatriksi, milles iga element on täisarv lõigust 1 - 75,
ning tagastab tõeväärtuse vastavalt sellele, kas arvud selles tabelis on veergudesse jaotatud vastavalt Bingo Loto
reeglitele.

Et tegu oleks korrektse Bingo Loto mänguväljaga, peavad vasakpoolseimas veerus olevad arvud kuuluma lõiku 1 - 15,
järgmises veerus olevad arvud lõiku 16 - 30 ja nii edasi, kuni viimases veerus on ainult arvud lõigust 61 - 75.

Lihtsuse mõttes võib siin ülesandes eeldada, et kõik arvud on antud tabelis unikaalsed ehk ükski arv ei esine tabelis
rohkem kui üks kord. Huvi korral proovige kontrollida ka arvude unikaalsust, et ei peetaks korrektseks tabelit, mis on
muidu reeglitele vastav, aga milles on kaks ühesugust arvu. Kui olete oma programmile lisanud unikaalsuse kontrolli,
siis peab funktsiooni nimeks olema on_bingo_tabel_extra

Näide:

on_bingo_tabel([
[1, 30, 34, 55, 75],
[10, 16, 40, 50, 67],
[5, 20, 38, 48, 61],
[4, 26, 43, 49, 70],
[15, 17, 33, 51, 66]
])
True

on_bingo_tabel([
[1, 30, 34, 55, 76],
[10, 16, 40, 50, 67],
[5, 20, 38, 48, 61],
[4, 26, 43, 49, 70],
[15, 17, 33, 51, 66]
])
False
"""


def on_bingo_tabel(table):
    result = True
    for j in range(5):
        for i in range(5):
            if (j * 15 + 1) <= table[i][j] <= ((j + 1) * 15):
                continue
            else:
                result = False
    return result

def on_bingo_tabel_extra(table):
    result = True
    bingo = []
    for j in range(5):
        for i in range(5):
            if table[i][j] in bingo:
                return False
            else:
                bingo.append(table[i][j])
            if (j * 15 + 1) <= table[i][j] <= ((j + 1) * 15):
                continue
            else:
                result = False
    return result


tableA = [
    [1, 30, 34, 55, 75],
    [10, 16, 40, 50, 67],
    [5, 20, 38, 48, 61],
    [4, 26, 43, 49, 70],
    [15, 17, 33, 51, 66]
]

tableB = [
    [1, 30, 34, 55, 76],
    [10, 16, 40, 50, 67],
    [5, 20, 38, 48, 61],
    [4, 26, 43, 49, 70],
    [15, 17, 33, 51, 66]
]

print(on_bingo_tabel(tableA))
print(on_bingo_tabel(tableB))

print("Extra:")
print(on_bingo_tabel_extra(tableA))
print(on_bingo_tabel_extra(tableB))

