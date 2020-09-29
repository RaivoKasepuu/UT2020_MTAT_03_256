"""
1.3 Kas on võitnud?
Tähtaeg: esmaspäev, 5. oktoober 2020, 23.59
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö
Järgnevad funktsioonid võtavad argumendiks 5 x 5 maatriksi, mis tähistab Bingo Loto tabelit ning milles iga element on kas täisarv lõigust 1 - 75 või suur trükitäht X. Täht X sümboliseerib seda, et vastav arv on mängus juba loositud.

1. Koostada funktsioon voitis_nurkademangu, mis tagastab tõeväärtuse vastavalt sellele, kas see mänguväli on võitnud nurkademängu: kõik mänguvälja nurgad on loositud.

2. Koostada funktsioon voitis_diagonaalidemangu, mis tagastab tõeväärtuse vastavalt sellele, kas see mänguväli on võitnud diagonaalidemängu: kõik mänguvälja diagonaalidel olevad arvud on loositud. Selleks koostada ja kasutada kahte abifunktsiooni:

Funktsioon x_peadiagonaalil, mis võtab argumendiks mänguvälja ja tagastab selle peadiagonaalil olevate X arvu.
Funktsioon x_korvaldiagonaalil, mis võtab argumendiks mänguvälja ja tagastab selle kõrvaldiagonaalil olevate X arvu.
3. Koostada funktsioon voitis_taismangu, mis tagastab tõeväärtuse vastavalt sellele, kas see mänguväli on võitnud täismängu: kõik mänguvälja arvud on loositud.

Bingo Loto reeglitega saab täpsemalt tutvuda siin: https://www.eestiloto.ee/osi/game/bingo/manual .
"""

def voitis_nurkademangu(tabel):
    if tabel[0][0] == "X" and tabel[0][4] == "X" and tabel[4][4] == "X" and tabel[4][0] == "X":
        return True
    else:
        return False

def x_peadiagonaalil(tabel):
    d = 0
    for i in range(5):
        if tabel[i][i] == "X":
            d += 1
    return d


def x_korvaldiagonaalil(tabel):
    d = 0
    for i in range(5):
        if tabel[i][-1-i] =="X":
            d += 1
    return d


def voitis_diagonaalidemangu(tabel):
    if x_peadiagonaalil(tabel) == 5 and x_korvaldiagonaalil(tabel) == 5:
        return True
    else:
        return False

def voitis_taismangu(tabel):

    q = 0
    for j in range(5):
        for i in range(5):
            if tabel[i][j] == "X":
                q += 1
    if q == 25:
        return True
    else:
        return False
