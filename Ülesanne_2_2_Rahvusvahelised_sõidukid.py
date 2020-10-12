"""
2.2 Rahvusvahelised sõidukid
Tähtaeg: esmaspäev, 19. oktoober 2020, 23.59
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö
Sõiduki registreerimismärgile või riigi tunnusmärgile on tavaliselt märgitud riigi tähis 1-3-tähelise lühendina. Eesti
puhul on lühendiks näiteks EST. Piirivalvel on andmebaas eri riikide tähistest tekstifailis nii, et faili igal real on
tühikuga eraldatud riigi tähis ja selle riigi nimi.

Väljavõte riigitähiste failist:
ER Eritrea
FIN Soome
F Prantsusmaa
H Ungari
LT Leedu
EST Eesti
S Rootsi


Koostada funktsioon failist_sonastik, mis võtab argumendiks andmebaasi faili nime ning tagastab vastava faili sisu
põhjal sõnastiku, kus võtmeteks on riigitähised (sõned) ja väärtusteks riikide nimed (sõned).

Koostada funktsioon tahised_nimedeks, mis võtab argumendiks järjendi riikide tähistest (sõned) ja eelmise funktsiooni
poolt koostatud sõnastiku ning tagastab järjendi vastavate riikide nimedest. Kui mõni tähis argumendiks antud järjendis
on tundmatu, siis selle riigi nimi tuleb asendada tagastatavas järjendis väärtusega None.

Rakendada funktsioone sobivalt programmis, mis
küsib kasutajalt andmebaasi faili nime,
küsib kasutajalt sõne, mis koosneb tühikutega eraldatud piiri ületanud sõidukite riikide tähistest,
väljastab sõidukite päritolumaade nimed üksteise alla. Kui mõni riigitähis on tundmatu, siis väljastada selle riigi
nime asemel Tundmatu maa.

Faili aasia.txt sisu

J Jaapan
SGP Singapur
IND India
LAO Laos
T Tai
CHN Hiina

korral

failist_sonastik("aasia.txt")
{'J': 'Jaapan', 'SGP': 'Singapur', 'IND': 'India', 'LAO': 'Laos', 'T': 'Tai', 'CHN': 'Hiina'}

tahised_nimedeks(['FIN', 'RUS', 'CHN', 'IND', 'F', 'LAO'], failist_sonastik("aasia.txt"))
[None, None, 'Hiina', 'India', None, 'Laos']

Faili lounaameerika.txt sisu

RA Argentiina
BR Brasiilia
UY Uruguai
CO Kolumbia

korral

failist_sonastik("lounaameerika.txt")
{'RA': 'Argentiina', 'BR': 'Brasiilia', 'UY': 'Uruguai', 'CO': 'Kolumbia'}

tahised_nimedeks(['EST', 'CO', 'FIN', 'UY', 'BR', 'BR', 'RA'], failist_sonastik("lounaameerika.txt"))
[None, 'Kolumbia', None, 'Uruguai', 'Brasiilia', 'Brasiilia', 'Argentiina']
"""
def failist_sonastik(fail):
    sonastik = {}
    with open(fail) as f:
        for line in f:
            (key, val) = line.split()
            sonastik[(key)] = val

        return(sonastik)


def tahised_nimedeks(list, sonastik):
    resultList = []
    # käime listi läbi ja leiame, kas listile vastab sonastikus riik
    for i in range(len(list)):
        if list[i] in sonastik:
            resultList.append(sonastik[list[i]])
        else:
            resultList.append(None)
    return resultList

# küsib kasutajalt andmebaasi faili nime,
fail = input("Sisesta andmebaasi faili nimi: ")
failist_sonastik(fail)

# küsib kasutajalt sõne, mis koosneb tühikutega eraldatud piiri ületanud sõidukite riikide tähistest
inputString = input("Sisestage piiri ületanud autode riikide tähised: ")
inputList = inputString.split(" ")

# väljastame sõidukite päritolumaade nimed üksteise alla.
# Kui mõni riigitähis on tundmatu, siis väljastada selle riigi nime asemel Tundmatu maa.

for i in range (len(tahised_nimedeks(inputList, failist_sonastik(fail)))):
    if tahised_nimedeks(inputList, failist_sonastik(fail))[i] == None:
        print("Tundmatu maa")
    else:
        print((tahised_nimedeks(inputList, failist_sonastik(fail))[i]))


# print(tahised_nimedeks(inputList, failist_sonastik("aasia.txt")))
# print(failist_sonastik("aasia.txt"))
# print(tahised_nimedeks(['FIN', 'RUS', 'CHN', 'IND', 'F', 'LAO'], failist_sonastik("aasia.txt")))