"""
3.5 Kasvavad read
Tähtaeg: esmaspäev, 2. november 2020, 23.59
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö
Järgnev programmilõik väljastab kahemõõtmelise arvude järjendi puhul, mitu rida on kasvavad s.t sellised, milles iga
järgnev element on suurem eelmisest:

jarjend_ruudus = [[4, 3, 2], [-1, 0]]

kasvavaid = 0
for rida in jarjend_ruudus:
    if len(rida) > 0:
        kasvav = True
        eelmine = rida[0]
        for el in rida[1:]:
            if el <= eelmine:
                kasvav = False
                break
            eelmine = el
        if kasvav:
            kasvavaid += 1

print("Kasvavaid ridu on " + str(kasvavaid))
Teie ülesanne on koostada funktsioon on_kasvav nii, et alltoodud programmilõik töötaks ülaltooduga võrdväärselt mistahes
kahemõõtmelise järjendi (jarjend_ruudus) puhul:

jarjend_ruudus = [[4, 3, 2], [-1, 0]]

kasvavaid = 0
for rida in jarjend_ruudus:
    kasvavaid += on_kasvav(rida)

print("Kasvavaid ridu on " + str(kasvavaid))
Toodud programmilõigule tuleb lisada funktsiooni on_kasvav definitsioon. Antud koodijupist on näha, kuidas seda
rakendatakse. Etteantud koodi muuta pole vaja. Kui korrektne definitsioon on lisatud, siis peaksid mõlemad koodilõigud
andma täpselt sama tulemuse (iga kahemõõtmelise arvude järjendi puhul).

Kontrollitakse vaid funktsiooni on_kasvav definitsiooni, selle rakendamist näitama ei pea.
"""


def on_kasvav(row):
    if not row:
        return 0
    else:
        result = 1
    if isinstance(row, list):
        for i in range(1, len(row)):
            if row[i - 1] >= row[i]:
                result = 0
                return result
            else:
                result = 1
    return result
