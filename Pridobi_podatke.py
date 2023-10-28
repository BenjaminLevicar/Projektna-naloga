import requests
import re

# funkcija za pridobitev htmljev, ki jih združujemo, da je koda kasneje hitrejša, saj ne bo treba toliko krat odpirati datoteke
for el in range(1, 101):
    for i in range(el*1000, (el+1)*1000):
        stran = requests.get(
            f'https://www.judoinside.com/judoka/{i}/judo-career'
        )
        with open(f'htmlji/skupek_strani{el+1}.html', 'a', encoding='utf-8') as dat:
            dat.write(stran.text)
