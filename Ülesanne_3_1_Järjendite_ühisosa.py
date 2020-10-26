"""
3.1 Järjendite ühisosa
Tähtaeg: esmaspäev, 2. november 2020, 23.59
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö
Koostada funktsioon yhisosa, mis võtab argumendiks kaks järjendit ja tagastab uue järjendi, mis sisaldab ühekordselt
neid elemente, mis esinesid mõlemas sisendjärjendis. Tagastatav järjend peab sisaldama ainult neid elemente, mis
eelnevale tingimusele vastavad.

Kontrollitakse vaid funktsiooni definitsiooni, programmis seda rakendama ei pea.
"""


def yhisosa(listOne, listTwo):
    resultList = []
    for i in range((len(listOne))):
        if listOne[i] in listTwo:
            resultList.append(listOne[i])
    return list(set(resultList))


print(yhisosa(['ich', 'du', 'er', 'sie', 'es'], ['wir', 'ihr', 'sie', 'Sie']))
print(yhisosa([], [1, 1]))
print(yhisosa([1, 1, 1], [1, 1]))
