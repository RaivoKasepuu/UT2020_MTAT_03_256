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

Näide:

>>> leidub_anagramm([['ab', 'ba']])
True

>>> leidub_anagramm([['ab', 'cad', 'cd'], ['abd', 'a', 'bd']])
False

>>> leidub_anagramm([['ab', 'cad', 'cd'], ['a', 'bad', 'bd']])
True

Vihje:
Mis tingimus on piisav selleks, et kaks sõne oleksid teineteise anagrammid? Pange tähele, et sõned koosnevad vaid
neljast erinevast märgist.
"""
# loeme võrreldavates sõnades üle tähed a,b,c,d ja kui need on võrdsed, on tegemist anagrammiga.