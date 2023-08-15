import re

with open('stran68054.html', encoding='utf-8') as dat:
    besedilo = dat.read()
    tekme = []
    for najdba in re.finditer(
        '<span>(?P<ime>\w*(\s\w*)+) Judoka</span>',
        besedilo,             
    ):
        tekme.append(najdba['ime'])
        
    for najdba in re.finditer(
        'Country: (?P<drzava>\w*)              </span>',
        besedilo,             
    ):
        tekme.append(najdba['drzava'])

print(tekme)        

with open('stranOnoNova.html', encoding='utf-8') as dat:
    besedilo = dat.read()
    tekme = []
    for najdba in re.finditer(
        '<td class="date">(?P<datum>\d*\s\w*\s\d*)</td>',
        besedilo,             
    ):
        tekme.append(najdba['datum'])
print(tekme)
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
            '<td class="date">' '.*?' '\s+<span></span>',
            flags=re.DOTALL,
            )
        for najdba in vzorec.finditer(besedilo):
            bloki.append(besedilo[najdba.start() : najdba.end()])

        return bloki
    


besedilo = poisci_bloke('stranOnoNova.html')
for el in besedilo:
    with open('podatkiNovo.html','a', encoding='utf-8') as dat:
        dat.write(el)

def izlusci_osebo(besedilo):
    oseba = {}
    
    vzorec_ime = re.compile('<span>(?P<ime>\w*(\s\w*)+) Judoka</span>')
    najdba_ime = vzorec_ime.search(besedilo)
    oseba['ime'] = najdba_ime['ime']
    
    vzorec_drzava = re.compile('Country: (?P<drzava>\w*)              </span>')
    najdba_drzava = vzorec_drzava.search(besedilo)
    oseba['drzava'] = najdba_drzava['drzava']
    
    return oseba
     


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
    
    vzorec_kategorija = re.compile('<td class="category">(?P<kategorija>U\d+)</td>')
    najdba_kategorija = vzorec_kategorija.search(blok)
    tekmovalec['kategorija'] = najdba_kategorija['kategorija']
    
    return tekmovalec

#besedilo = poisci_bloke('stran.html')
#for blok in besedilo:
#    #i = 1
#    #if i >= len(tekme):
#    #    break 
#    print(izlusci_podatke(blok))

besedilo = 'stran68054.html'
#print(izlusci_osebo(besedilo))