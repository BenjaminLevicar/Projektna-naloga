import re

with open('stran68054.html', encoding='utf-8') as dat:
    besedilo = dat.read()
    tekme = []
    for najdba in re.finditer(
        '<td class="result">(?P<rezultat>\d+)</td>',
        besedilo,             
    ):
        tekme.append({'rezultat': najdba['rezultat']})
        

bloki = []
with open('stran68054.html', encoding='utf-8') as dat:
    besedilo = dat.read()
    vzorec = re.compile(
        '<td class="date">' '.*?' '\s+</tr>',
        flags=re.DOTALL,
    ) 
    with open('podatki.html', 'a', encoding='utf-8') as dat:
        for najdeno in vzorec.finditer(besedilo):
            dat.write(besedilo[najdeno.start(): najdeno.end()])

print(bloki)
        
print(tekme)