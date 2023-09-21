import re
import typing

#def poisci_bloke(tekst):
#    bloki = []
#    with open(tekst, encoding='utf-8') as dat:
#        besedilo = dat.read()
#        vzorec = re.compile(
#            '<tr class="body">' '.*?' '                </tr>',
#            flags=re.DOTALL,
#            )
#        for najdba in vzorec.finditer(besedilo):
#            bloki.append(besedilo[najdba.start() : najdba.end()])
#
#        return bloki
#
#
#def izlusci_podatke(blok):
#    medalje = {}
#    
#    vzorec_drzava = re.compile('<td class="name">(?P<drzava>[\w*\s?]*)</td>')
#    najdba_drzava = vzorec_drzava.search(blok)
#    medalje['drzava'] = najdba_drzava['drzava']
#    
#    vzorec_zlata = re.compile('<td class="gold">(?P<zlata>\d*)</td>')
#    najdba_zlata = vzorec_zlata.search(blok)
#    medalje['zlata'] = najdba_zlata['zlata']
#    
#    vzorec_srebrna = re.compile('<td class="silver">(?P<srebrna>\d*)</td>')
#    najdba_srebrna = vzorec_srebrna.search(blok)
#    medalje['srebrna'] = najdba_srebrna['srebrna']
#    
#    vzorec_bronasta = re.compile('<td class="bronze">(?P<bronasta>\d*)</td>')
#    najdba_bronasta = vzorec_bronasta.search(blok)
#    medalje['bronasta'] = najdba_bronasta['bronasta']
#    
#    vzorec_skupno = re.compile('<td class="total">(?P<skupno>\d*)</td>')
#    najdba_skupno = vzorec_skupno.search(blok)
#    medalje['skupno'] = najdba_skupno['skupno']
#    
#    return medalje
#a = []
#for blok in poisci_bloke('podatki_o_tekmi.html'):
#    print(izlusci_podatke(blok))
    
def poisci_bloke(tekst):
    bloki = []
    with open(tekst, encoding='utf-8') as dat:
        besedilo = dat.read()
        vzorec = re.compile(
            '<td class="date">' '.*?' '                  </tr>',
            flags=re.DOTALL,
            )
        for najdba in vzorec.finditer(besedilo):
            bloki.append(besedilo[najdba.start() : najdba.end()])

        return bloki
    
def izlusci_podatke(blok):
    tekmovalec = {}

    vzorec_datum = re.compile(r'<td class="date">(?P<datum>\d*\s\w*\s\d*)</td>')
    najdba_datum = vzorec_datum.search(blok)
    try:
        tekmovalec['datum'] = najdba_datum['datum']
    except:
        tekmovalec['datum'] = '/'
    
    vzorec_rezultat = re.compile(r'<td class="result">(?P<rezultat>\d+)</td>')
    najdba_rezultat = vzorec_rezultat.search(blok)
    try:
        tekmovalec['rezultat'] = najdba_rezultat['rezultat']
    except:
        tekmovalec['rezultat'] = '/'
    
    vzorec_dogodek = re.compile(r'<a class="details-link" href="/event/\d+/\w+">(?P<dogodek>(\'?\w+(\'\w)?\s*\-?\'?)+)</a>')
    najdba_dogodek = vzorec_dogodek.search(blok)
    try:
        tekmovalec['dogodek'] = najdba_dogodek['dogodek']
    except:
        tekmovalec['dogodek'] = '/'
    

    vzorec_kategorija = re.compile(r'<td class="category">(?P<kategorija>\w+\d+)</td>')
    najdba_kategorija = vzorec_kategorija.search(blok)
    try:
        tekmovalec['kategorija'] = najdba_kategorija['kategorija']
    except:
        tekmovalec['kategorija'] = '/'

    return tekmovalec

for i in range(1, 11):        
    with open(f'htmlji/stran{i}.html', encoding='utf-8') as dat:
        with open('rezultati.html', 'a', encoding='utf-8') as dato:
            besedilo = dat.read()
            tekme = []
            for najdba in re.finditer(
                '<span>(?P<ime>\w*(\s\w*)+) Judoka</span>',
                besedilo,             
            ):
                tekme.append(najdba['ime'])
                a = najdba['ime']
            for najdba in re.finditer(
                'Country: (?P<drzava>\w*)              </span>',
                besedilo,             
            ):
                tekme.append(najdba['drzava'])
            for blok in poisci_bloke(f'htmlji/stran{i}.html'):
                tekma = izlusci_podatke(blok)
                if tekma['datum'] == '/' or tekma['rezultat'] == '/' or tekma['dogodek'] == '/' or tekma['kategorija'] == '/':
                    break
                tekma['ime'] = a
                dato.write(str(tekma) + '\n')