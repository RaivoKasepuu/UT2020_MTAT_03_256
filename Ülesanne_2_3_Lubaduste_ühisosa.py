"""
2.3 Lubaduste ühisosa
Tähtaeg: esmaspäev, 19. oktoober 2020, 23.59
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö
Iga erakonna valimislubadused on kirja pandud hulgana, näiteks nii:

erakond_A = {"lastetoetusi tõsta", "pensione tõsta", "tulumaksu langetada", "kaitsekulutusi tõsta"}
erakond_B = {"muuta kõike varasemat"}
erakond_C = {"sisserännet piirata", "pensione tõsta", "kaitsekulutusi tõsta"}
erakond_D = set()
erakond_E = {"väljarännet piirata", "pensione tõsta", "õpetajate palku tõsta", "kaitsekulutusi tõsta",
"alkoholiaktsiisi tõsta"}

Eesmärk on leida kaks erakonda, mis lubaduste poolest kõige enam sarnanevad. Selleks tuleb leida kaks hulka, mille
ühisosa on kõige suurem.

Koostada funktsioon kooslubajad, mis võtab argumendiks järjendi erakondade lubaduste hulkadest ja tagastab paarina
(kaheelemendilise ennikuna) nende kahe erakonna indeksid järjendis, mille lubadustel on kõige suurem ühisosa. Kui
selliseid paare on mitu, siis võib neist ükskõik millise tagastada.

Kontrollitakse vaid funktsiooni definitsiooni, programmis seda rakendama ei pea.

kooslubajad([{"maamaks kaotada", "pensione tõsta", "kaitsekulutusi tõsta"}, {"lasteaiaõpetajate palku tõsta",
"kindlustada tasuta hambaravi kuni 30-aastastele"}, {"sisserännet piirata", "pensione tõsta", "kaitsekulutusi tõsta"},
set()])
(0, 2)

kooslubajad([{"arstide palku tõsta", "pensione tõsta", "kaitsekulutusi tõsta"}, {"lasteaiaõpetajate palku tõsta",
"motosporti toetada"}, {"sisserännet piirata", "pensione tõsta", "arstide palku tõsta",
"lasteaiaõpetajate palku tõsta"}, {"arstide palku tõsta", "tuletõrjujate palku tõsta", "politsenike palku tõsta",
"piirivalvurite palku tõsta", "vangivalvurite palka tõsta"}])
(0, 2)

kooslubajad([{"algatada koduloometoetus", "kuritegevust vähendada", "kõiki toetusi suurendada",
"kaotada kõik maksud", "suurendada kõiki palkasid", "rajada spordiväljakud igasse linna"}, {"toetada pensionäre",
"aidata noorperesid", "edendada maaelu", "suurendada vastsündinute arvu", "vähendada suremust"}])
(0, 1)
"""
def kooslubajad(list):
    # initsialiseerime muutujad
    max = 0
    maxi = 0
    maxj = 0
    # vastused korjame listi
    resultList = []

    for i in range(len(list)):
        for j in range(len(list)):
            if i == j:
                continue
            else:
                yhisosa = list[i].intersection(list[j])
                if len(yhisosa) > max:
                    max = len(yhisosa)
                    maxi = i
                    maxj = j
    # erijuhtum: listis vaid 2 elementi:
    if len(list) == 2:
        maxi = 0
        maxj = 1
    # lisame listi indeksid resultListi:
    resultList.append(maxi)
    resultList.append(maxj)
    # teeme listist tuple, sest nii oli nõutud
    resultTuple = tuple(resultList)
    return resultTuple


print(kooslubajad([{"algatada koduloometoetus", "kuritegevust vähendada", "kõiki toetusi suurendada",
"kaotada kõik maksud", "suurendada kõiki palkasid", "rajada spordiväljakud igasse linna"}, {"toetada pensionäre",
"aidata noorperesid", "edendada maaelu", "suurendada vastsündinute arvu", "vähendada suremust"}]))

print(kooslubajad([{"maamaks kaotada", "pensione tõsta", "kaitsekulutusi tõsta"}, {"lasteaiaõpetajate palku tõsta",
"kindlustada tasuta hambaravi kuni 30-aastastele"}, {"sisserännet piirata", "pensione tõsta", "kaitsekulutusi tõsta"},set()]))

print(kooslubajad([{"arstide palku tõsta", "pensione tõsta", "kaitsekulutusi tõsta"}, {"lasteaiaõpetajate palku tõsta",
"motosporti toetada"}, {"sisserännet piirata", "pensione tõsta", "arstide palku tõsta",
"lasteaiaõpetajate palku tõsta"}, {"arstide palku tõsta", "tuletõrjujate palku tõsta", "politsenike palku tõsta",
"piirivalvurite palku tõsta", "vangivalvurite palka tõsta"}]))
