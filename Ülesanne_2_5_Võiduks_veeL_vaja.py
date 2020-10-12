"""
2.5 Võiduks veel vaja
Tähtaeg: esmaspäev, 19. oktoober 2020, 23.59
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö
Järgnevad funktsioonid võtavad argumendiks 5 x 5 maatriksi, mis tähistab Bingo Loto tabelit ning milles iga element on
kas täisarv lõigust 1 - 75 või suur trükitäht X. Täht X sümboliseerib seda, et vastav arv on mängus juba loositud.

1. Koostada funktsioon nurkademanguks_vaja, mis tagastab järjendi arvudest, mida on veel vaja loosida selleks, et antud
mänguväli võidaks nurkademängu.

2. Koostada funktsioon diagonaalidemanguks_vaja, mis tagastab järjendi arvudest, mida on veel vaja loosida selleks, et
antud mänguväli võidaks diagonaalidemängu.

3. Koostada funktsioon taismanguks_vaja, mis tagastab järjendi arvudest, mida on veel vaja loosida selleks, et antud
mänguväli võidaks täismängu.

Kontrollitakse vaid funktsioonide definitsioone, programmis neid rakendama ei pea.

Abiks võib olla video.

"""
def nurkademanguks_vaja(bingo):
    corners = []
    for i in range(0, 5, 4):
        for j in range(0, 5, 4):
            if bingo[i][j] != "X":
                corners.append(bingo[i][j])
    return corners


def diagonaalidemanguks_vaja(bingo):
    diagonal = []
    for i in range(5):
        for j in range(5):
            if (i == j and bingo[i][j] != "X") or (i + j == 4 and bingo[i][j] != "X"):
                diagonal.append(bingo[i][j])
    return diagonal


def taismanguks_vaja(bingo):
    full = []
    for i in range(5):
        for j in range(5):
            if bingo[i][j] != "X":
                full.append(bingo[i][j])
    return full
