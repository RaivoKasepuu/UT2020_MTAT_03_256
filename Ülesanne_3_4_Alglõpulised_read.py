"""
3.4 Alglõpulised read
Tähtaeg: esmaspäev, 2. november 2020, 23.59
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö
Järgnev programmilõik väljastab kahemõõtmelise arvude järjendi puhul, mitu rida on sellised, milles esimene element on
suurem kui viimane element:

jarjend_ruudus = [[4, 3, 2], [-1, 0]]

alglopulisi = 0
for rida in jarjend_ruudus:
    if len(rida) > 1:
        if rida[0] > rida[-1]:
            alglopulisi += 1

print("Alglõpulisi ridu on " + str(alglopulisi))
Teie ülesanne on koostada funktsioon on_alglopuline nii, et alltoodud programmilõik töötaks ülaltooduga võrdväärselt
mistahes kahemõõtmelise järjendi (jarjend_ruudus) puhul:

jarjend_ruudus = [[4, 3, 2], [-1, 0]]

alglopulisi = 0
for rida in jarjend_ruudus:
    alglopulisi += on_alglopuline(rida)

print("Alglõpulisi ridu on " + str(alglopulisi))
Toodud programmilõigule tuleb lisada funktsiooni on_alglopuline definitsioon. Antud koodijupist on näha, kuidas seda
rakendatakse. Etteantud koodi muuta pole vaja. Kui korrektne definitsioon on lisatud, siis peaksid mõlemad koodilõigud
andma täpselt sama tulemuse (iga kahemõõtmelise arvude järjendi puhul).

Kontrollitakse vaid funktsiooni on_alglopuline definitsiooni, selle rakendamist näitama ei pea.
"""

def on_alglopuline(row):
    if len(row) == 0:
        return 0
    if row[0] > row[-1]:
        return 1
    else:
        return 0


row = [[4, 3, 2], [-1, 0]]
print(on_alglopuline(row))
row = [[4, 3, 2]]
print(on_alglopuline(row))
row = [[4, 3, 2], [1, 0]]
print(on_alglopuline(row))
