"""
1.6 Anagrammi otsing
Tähtaeg: esmaspäev, 5. oktoober 2020, 23.59
Maksimaalne failide arv: 1
Töö liik: Individuaaltöö
Koostada funktsioon leidub_anagramm, mis võtab argumendiks sõnede maatriksi kahemõõtmelise järjendina, milles sõned
koosnevad vaid tähtedest a, b, c ja d. Funktsioon tagastab tõeväärtuse vastavalt sellele, kas selles maatriksis leidub
element, mis on sellise sõne anagramm, mis on saadud temast vahetult vasakul ja vahetult paremal olevate sõnede
kokkukirjutamise teel.

Kui vasakul või paremal elementi ei leidu, siis tuleb seda arvestada tühja sõnena.

Kontrollitakse vaid funktsiooni definitsiooni, programmis seda rakendama ei pea.

"""
def leidub_anagramm(matrix):
# käime matrixi üksipulki läbi:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            testString = ""
            if j > 0:
                testString += matrix[i][j - 1]
            if j < len(matrix[i]) - 1:
                testString += matrix[i][j + 1]
            # kasutame sorted() meetodit, et elemendid oleksid tähestikulises järjekorras, 1:1 võrreldavad
            if sorted(testString) == sorted(matrix[i][j]):
                return True
    return False

print(([['karuperse', 'persekaru']]))
print(leidub_anagramm([['karuperse', 'persekaru']]))
print(([['karuperse', 'persekarv']]))
print(leidub_anagramm([['karuperse', 'persekarv']]))
