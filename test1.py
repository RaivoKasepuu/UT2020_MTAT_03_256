"""

def genereeri_sona(sonad, index):
    uus_sona = ''
    for sona in sonad:
        if len(sona) > index:
            uus_sona += sona[index]
    return uus_sona
print(genereeri_sona(['putukas', 'kollane', 'programm', 'lihtne', 'samm'],4))

def sulgude_avamine(jar_1, jar_2):
    tulemus = 0
    for k_1 in jar_1:
        for k_2 in jar_2:
            tulemus += k_1 * k_2
    return tulemus

liikmed_1 = [3,5]
liikmed_2 = [0,1]

print(sulgude_avamine(liikmed_1, liikmed_2))
"""

def maatriks (m,n,e):
    tabel = []
    for i in range(n):
        rida = []
        for j in range(m):
            rida.append(e)
        tabel.append(rida)
    return tabel

esimene = maatriks(3,2,'@')
teine = maatriks(2,3,0)

print(len(teine + esimene))
