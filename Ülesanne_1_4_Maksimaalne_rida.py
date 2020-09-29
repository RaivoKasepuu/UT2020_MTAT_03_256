"""
1.4 Maksimaalne rida
Tähtaeg: esmaspäev, 5. oktoober 2020, 23.59
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö
On antud fail, kus igal real on tühikutega eraldatud täisarvud. Arvude hulk ridadel võib olla erinev. Eesmärk on igal real olevad arvud kokku liita ja leida saadud summadest suurim.

Koostada programm, mis

küsib kasutajalt failinime,

leiab, mis rida failist sisaldab kõige suuremat summat,

väljastab suurima summaga rea järjekorranumbri ja vastava summa ekraanile.

Ridade järjekorranumbrid algavad tavapäraselt ühest.

Näide:

Faili arvud.txt sisu:

5 10 5
0 0 -1 100
-10
1 1 1 1 1 1 1 1 1 1
42

Programmi töö:

Sisestage failinimi: arvud.txt

Suurim summa on failis 2. real ja see on 99.

"""
file = input("Sisesta andmete faili nimi: ")
file = open(file, encoding="UTF-8")

table = []
for row in file:  # iga rea jaoks failist
    numbrid = []
    osad = row.split()
    for osa in osad:  # osade kaupa
        numbrid.append(int(osa))
    table.append(numbrid)
file.close()

# teeme eraldi järjendi r[] tabeli ridade summadest
r = []

for i in range(len(table)):
    s = 0
    for j in range(len(table[i])):
        s = s + table[i][j]
    r.append(s)

# leiame max summaga rea numbri
maximum = r[0]
index = 0
for k in range(len(r)):
    if r[k] > maximum:
        maximum = r[k]
        index = k
print("Suurim summaga on failis " + str(1 + index) + ". real ja see on " + str(maximum))
