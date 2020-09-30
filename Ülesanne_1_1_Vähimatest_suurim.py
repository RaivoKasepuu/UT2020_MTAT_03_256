"""
1.1 Vähimatest suurim
Tähtaeg: esmaspäev, 5. oktoober 2020, 23.59
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö
Koostada funktsioon vahimatest_suurim, mis võtab argumendiks täisarvude maatriksi kahemõõtmelise järjendina ja tagastab antud maatriksist kõikide ridade vähimatest elementidest suurima.

Teisisõnu peab tagastatav element olema

vähim element oma reas,
suurim element kõikide selliste elementide seas, mis on oma reas vähimad.
Kontrollitakse vaid funktsiooni definitsiooni, programmis seda rakendama ei pea.

Näide:

>>> vahimatest_suurim([[3, 0], [0, -1], [2, 1]])
1

>>> vahimatest_suurim([[3, 0], [0, -1], [2, 2]])
2

>>> vahimatest_suurim([[3, 0]])
0

>>> vahimatest_suurim([[0], [1], [2], [3], [-1]])
3
"""
def vahimatest_suurim(maatriks):
    # võtame esimese rea väikseima võrdluse aluseks:
    maxsmallest = min(maatriks[0])
    # leiame iga rea vähima ja võrdleme neid senise vähimaga
    for row in maatriks:
        smallest = min(row)
        if smallest > maxsmallest:
            maxsmallest = smallest
    return maxsmallest

A = [[3, 0], [0, -1], [2, 1]]
B = [[3, 0], [0, -1], [2, 2]]
C = [[3, 0]]
D = [[0], [1], [2], [3], [-1]]

print(A)
print("vähimatest suurim element on "+str(vahimatest_suurim(A)))
print()
print(B)
print("vähimatest suurim element on "+str(vahimatest_suurim(B)))
print()
print(C)
print("vähimatest suurim element on "+str(vahimatest_suurim(C)))
print()
print(D)
print("vähimatest suurim element on "+str(vahimatest_suurim(D)))
