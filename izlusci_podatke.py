import re

with open('stran68054.html', encoding='utf-8') as dat:
    besedilo = dat.read()
    tekme = []
    for najdba in re.finditer(
        '<a class="details-link" href="/event/\d+/\w+">(?P<tekma>\w*)</a>                    </td>',
        besedilo,             
    ):
        print(najdba['tekma'])
        

#bloki = []
#with open('stran68054.html', encoding='utf-8') as dat:
#    besedilo = dat.read()
#    vzorec = re.compile(
#        '<td class="date">' '.*?' '\s+</tr>',
#        flags=re.DOTALL,
#    ) 
#    with open('podatki.html', 'a', encoding='utf-8') as dat:
#        for najdeno in vzorec.finditer(besedilo):
#            dat.write(besedilo[najdeno.start(): najdeno.end()])
#
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
    vzorec = re.compile(
        '<td class="date">' '.*?' '\s+</tr>',
        flags=re.DOTALL,
    ) 

    for najdba in vzorec_bloka.finditer(besedilo):
        bloki.append(besedilo[najdba.start() : najdba.end()])

    return bloki


#with open('podatki.html', encoding='utf-8') as dat:
#def izlusci_podatke(blok):
#    tekovalec = {}
#    
#    vzorec_datum = re.compile('<td class="date">(?P<datum>\d*\s\w*\s\d*)</td>')
#    najdba_datum = vzorec_datum.search(blok)
#    tekmovalec['datum'] = najdba_datum['datum']
#    
#    vzorec_rezultat = re.compile('<td class="result">(?P<rezultat>\d+)</td>')
#    najdba_rezultat = vzorec_rezultat.search(blok)
#    tekmovalec['rezultat'] = najdba_rezultat['rezultat']
#    
#    vzorec_dogodek = re.compile('<a class="details-link" href="/event/\d*/\w*">(?P<tekma>\w*)</a>')