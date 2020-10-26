"""
3.2 Listid sõnastikuks
Tähtaeg: esmaspäev, 2. november 2020, 23.59
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö
Koostada funktsioon listid_sonastikuks, mis võtab argumendiks kaks ühepikkust järjendit ja tagastab nende põhjal
moodustatud sõnastiku, kus võtmeteks on esimese järjendi elemendid ja väärtusteks teise järjendi vastavatel
positsioonidel olevad elemendid.

Kui esimeses (võtmete) järjendis on korduvaid elemente, siis sõnastikku tuleb panna neist viimane koos vastava
elemendiga väärtuste järjendist. Teisisõnu kirjutavad sama võtmega kirjed eelnevaid väärtuseid üle nagu sõnastiku puhul
ikka kombeks.

Kontrollitakse vaid funktsiooni definitsiooni, programmis seda rakendama ei pea.
"""

def listid_sonastikuks(listOne, listTwo):
    resultDict = {}
    for i in range(len(listOne)):
        resultDict[listOne[i]] = listTwo[i]
    return resultDict

print(listid_sonastikuks([1, 2], [3, 4]))
print(listid_sonastikuks(['ATI', 'KAMA'], ['Arvutiteaduse instituut', 'Kasutatav masintõlge']))
print(listid_sonastikuks([0, 1, 0], ['a', 'b', 'c']))
