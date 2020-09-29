"""
1.5 Sudoku lahenduse kontrollimine
Tähtaeg: esmaspäev, 5. oktoober 2020, 23.59
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö
Failis on lahendatud Sudoku tabel esitatud nii, et kokku on 9 rida ja igas reas on tühikutega eraldatud 9 arvu. Sudoku mängureeglitega saab tutvuda näiteks siin.

Koostada programm, mis

küsib kasutajalt failinime,
kontrollib, kas vastavas failis antud Sudoku lahendus on korrektne:
kui lahendus on korrektne, siis väljastab ekraanile OK või
kui lahendus on mittekorrektne, siis väljastab ekraanile VIGA.
Teile on juba ette antud (teise programmeerija poolt koostatud) kõikide 3x3 kastide kontrollimise funktsioon. Uurige, kuidas see töötab ja rakendage seda oma programmis sobivalt. Programmile tuleb ise lisada ridade ja veergude kontrollimine.

 Kastide kontrollimise funktsioon

 def kastid_korras(maatriks):
    # Vaatame igat 3x3 kasti
    for rea_nurk in range(0, 9, 3):
        for veeru_nurk in range(0, 9, 3):
            # Iga kasti korral kogume tema elemendid järjendisse 'kast'
            kast = []
            for i in range(3):
                for j in range(3):
                    kast.append(int(maatriks[rea_nurk + i][veeru_nurk + j]))
            # Ja kontrollime, kas elemendid on korrektsed
            if sorted(kast) != list(range(1, 10)):
                return False
    return True

Kui failist loetud lahendus on mittekorrektne, siis võite soovi korral väljastada ka info vea asukoha kohta, näiteks mis reas ja veerus viga asub, kuid see ei ole kohustuslik.



Näide:

Näide 1

Faili korrektne.txt sisu:

3 2 7 4 8 1 6 5 9
1 8 9 3 6 5 7 2 4
6 5 4 2 7 9 8 1 3
7 9 8 1 3 2 5 4 6
5 6 3 9 4 7 2 8 1
2 4 1 6 5 8 3 9 7
8 1 2 7 9 3 4 6 5
4 7 5 8 1 6 9 3 2
9 3 6 5 2 4 1 7 8
Programmi töö:

Sisestage failinimi: korrektne.txt

OK

Näide 2

Faili ebakorrektne.txt sisu:

3 2 7 4 8 1 6 5 9
1 8 9 3 6 5 7 2 4
6 5 4 2 7 9 8 1 3
7 9 8 1 3 2 5 4 6
5 6 3 9 4 7 2 8 1
1 4 1 6 5 8 3 9 7
8 1 2 7 9 3 4 6 5
4 7 5 8 1 6 9 3 2
9 3 6 5 2 4 1 7 8
Programmi töö:

Sisestage failinimi: ebakorrektne.txt

VIGA. Viga asub 6. real, 1. veerus.

Vihjeid:
Kastide korrektsuse kontrollimise funktsioon on abiks mitmel moel. Muidugi saab tema abil kontrollida, kas kastidega on
kõik korras. Samuti aga võib saada vihjeid, kuidas üldse kontrollida, kas järjendis on täpselt kõik täisarvud 1-st 9-ni.

Ridade korrektsuse kontrolli puhul saab kasutada asjaolu, et iga rida lahenduses ongi eraldi järjend, kui esitame
tabelit kahemõõtmelise järjendina.

Silmas tuleb pidada, et mittekorrektsuse saab kindlaks lugeda juba esimese leitud ebakõla juures, korrektsuse aga alles
siis, kui kõik on kontrollitud.
"""


def kastid_korras(maatriks):
    # Vaatame igat 3x3 kasti
    for rea_nurk in range(0, 9, 3):
        for veeru_nurk in range(0, 9, 3):
            # Iga kasti korral kogume tema elemendid järjendisse 'kast'
            kast = []
            for i in range(3):
                for j in range(3):
                    kast.append(int(maatriks[rea_nurk + i][veeru_nurk + j]))
            # Ja kontrollime, kas elemendid on korrektsed
            if sorted(kast) != list(range(1, 10)):
                return False
    return True


# kontrollime veergude summat (peab olema igal veerul 45):

def ridade_kontroll(maatriks):
    for i in range(9):
        summa = 0
        for j in range(9):
            summa += maatriks[i][j]
        if summa != 45:
            return False
    return True


# kontrollime ridade summat (peab olema igal real 45):
def veergude_kontroll(maatriks):
    for j in range(9):
        summa = 0
        for i in range(9):
            summa += maatriks[i][j]
        if summa != 45:
            return False
    return True


fail = input("sisesta sudoku faili nimi: ")
fail = open(fail, encoding="UTF-8")

# fail = open("sudokuviga2.txt", encoding="UTF-8")

maatriks = []
for rida in fail:  # iga rea jaoks failist
    numbrid = []
    osad = rida.split()
    for osa in osad:  # osade kaupa
        numbrid.append(int(osa))
    maatriks.append(numbrid)
fail.close()

if kastid_korras(maatriks) == True and ridade_kontroll(maatriks) == True and veergude_kontroll(maatriks) == True:
    print("OK")
else:
    print("VIGA")

