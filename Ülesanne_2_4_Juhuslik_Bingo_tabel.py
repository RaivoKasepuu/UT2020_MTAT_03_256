"""
2.4 Juhuslik Bingo tabel
Tähtaeg: esmaspäev, 19. oktoober 2020, 23.59
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö
Koostada ilma argumentideta funktsioon juhuslik_bingo, mis tagastab juhuslikult genereeritud korrektse Bingo Loto
tabeli, kus pole ühtegi ruutu veel märgitud/loositud.

Oma lahenduse kontrollimiseks saab kasutada ülesande Reeglite kontrollimine lahendusfunktsiooni.

Erinevalt reeglite kontrollimise ülesandest siin ülesandes lihtsustavat arvude unikaalsuse eeldust ei tehta. Seega on
oluline tähele panna, et ükski arv ei tohi veerus (ega terves tabelis) korduda. Arvude genereerimiseks võib kasutada
moodulist random funktsiooni sample. Komplekti arvudest esimese Bingo tabeli veeru jaoks saaks selle abil genereerida
nii: sample(range(1, 16), 5).

Kontrollitakse vaid funktsiooni definitsiooni, programmis seda rakendama ei pea.

juhuslik_bingo()
[[2, 30, 34, 55, 75], [10, 19, 40, 50, 67], [5, 20, 38, 48, 61], [4, 26, 43, 49, 70], [15, 17, 33, 51, 66]]
"""
import random

def juhuslik_bingo():
    # initsialiseerime maatriksid
    matrix = []
    resultMatrix = [[0 for i in range(5)] for j in range(5)]
    for i in range(1, 6):
        rida = random.sample(range((i - 1) * 15 + 1, 15 * i), 5)
        matrix.append(rida)
    # pöörame maatriksit 90 kraadi, et vastaks bingo tingimustele
    for i in range(5):
        for j in range(5):
            resultMatrix[i][j] = matrix[j][i]
    return resultMatrix

print(juhuslik_bingo())