"""
2.1 Teksti analüüs
Tähtaeg: esmaspäev, 19. oktoober 2020, 23.59
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö
Koostada funktsioon symbolite_sagedus, mis võtab argumendiks sõne ja tagastab sõnastiku, mis sisaldab selles sõnes
esinevate tähemärkide esinemiste sagedusi. Tagastatav sõnastik peab seega sisaldama kirjeid, kus võtmeteks on
ühetähemärgilised sõned (sümbolid) ja väärtusteks vastavate sõnede (sümbolite) esinemiste arv argumendiks antud sõnes.

Pange tähele, et sümbolite alla käivad kõik pikkusega 1 sõned, mis argumendiks antud sõnes sisalduvad, sh tühikud ja
kirjavahemärgid. Samuti loetakse erinevateks sümboliteks näiteks väike täht a ja suur täht A.

Kontrollitakse vaid funktsiooni definitsiooni, programmis seda rakendama ei pea.

symbolite_sagedus("Hommikul silmad on kinni ja huulil on naer")
{'H': 1, 'o': 3, 'm': 3, 'i': 5, 'k': 2, 'u': 3, 'l': 4, ' ': 7, 's': 1, 'a': 3, 'd': 1, 'n': 5, 'j': 1, 'h': 1,
'e': 1, 'r': 1}

symbolite_sagedus("suitsupääsuke")
{'s': 3, 'u': 3, 'i': 1, 't': 1, 'p': 1, 'ä': 2, 'k': 1, 'e': 1}

symbolite_sagedus("l@htek00d")
{'l': 1, '@': 1, 'h': 1, 't': 1, 'e': 1, 'k': 1, '0': 2, 'd': 1}
"""
def symbolite_sagedus(string):
    sonastik = {}
    for i in range(len(string)):
        char = string[i]
        if char in sonastik:
            # suurendame char-i loendurit
            sonastik[char] += 1
        else:
            # lisame char-i sõnastikku
            sonastik[char] = 1
    return sonastik

print(symbolite_sagedus("Hommikul silmad on kinni ja huulil on naer"))
print(symbolite_sagedus("suitsupääsuke"))
print(symbolite_sagedus("l@htek00d"))
