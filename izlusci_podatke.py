import re

#with open('stran68054.html', encoding='utf-8') as dat:
#    besedilo = dat.read()
#    tekme = []
#    for najdba in re.finditer(
#        '<td class="date">(?P<datum>\d*\s\w*\s\d*)</td>',
#        besedilo,             
#    ):
#        tekme.append(najdba['datum'])
#print(tekme)        

#bloki = []
#with open('stran68054.html', encoding='utf-8') as dat:
#    besedilo = dat.read()
#    vzorec = re.compile(
#        '<tr class="body">' '.*?' '\s+</tr>',
#        flags=re.DOTALL,
#    ) 
#    with open('podatki.html', 'a', encoding='utf-8') as dat:
#        for najdeno in vzorec.finditer(besedilo):
#            dat.write(besedilo[najdeno.start(): najdeno.end()])

#print(bloki)
        
#print(tekme)

#kategorija = []
#mesto = []
#
#with open('podatki.html', encoding='utf-8') as dat:
#    besedilo = dat.read()
#    for najdba in re.finditer(
#        '<td class="result">(?P<rezultat>\d+)</td>',
#        besedilo,             
#    ):
#        mesto.append(najdba['rezultat'])
#    for najdba in re.finditer(
#        '<td class="category">(?P<kategorija>\w\d+)</td>',
#        besedilo,
#    ):
#        kategorija.append(najdba['kategorija'])
#
#print(len(kategorija))
#print(len(mesto))


def poisci_bloke(tekst):
    bloki = []
    with open(tekst, encoding='utf-8') as dat:
        besedilo = dat.read()
        vzorec = re.compile(
            '<tr class="body">' '.*?' '\s+</tr>',
            flags=re.DOTALL,
            )
        for najdba in vzorec.finditer(besedilo):
            bloki.append(besedilo[najdba.start() : najdba.end()])

        return bloki

#print(poisci_bloke('stran68054.html'))


def izlusci_podatke(blok):
    tekmovalec = {}
    
    vzorec_datum = re.compile('<td class="date">(?P<datum>\d*\s\w*\s\d*)</td>')
    najdba_datum = vzorec_datum.search(blok)
    tekmovalec['datum'] = najdba_datum['datum']
    #if najdba_datum['datum'] is None:
    #    tekmovalec['datum'] = r'/'
    #else:
    
    vzorec_rezultat = re.compile('<td class="result">(?P<rezultat>\d+)</td>')
    najdba_rezultat = vzorec_rezultat.search(blok)
    tekmovalec['rezultat'] = najdba_rezultat['rezultat']
    
    vzorec_dogodek = re.compile('<a class="details-link" href="/event/\d+/\w+">(?P<dogodek>(\w+\s*)+)</a>')
    najdba_dogodek = vzorec_dogodek.search(blok)
    tekmovalec['dogodek'] = najdba_dogodek['dogodek']
    
    return tekmovalec

besedilo = poisci_bloke('stran68054.html')
for blok in besedilo:
    #i = 1
    #if i >= len(tekme):
    #    break 
    print(izlusci_podatke(blok))