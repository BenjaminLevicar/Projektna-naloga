import re

# poiščemo html ene spletne strani, ime ter drzavo v datoteki z večimi
def poisci_strani(tekst):
    stran = []
    with open(tekst, encoding='utf-8') as dat:
        besedilo = dat.read()
        vzorec = re.compile(
            '<!DOCTYPE html>' '.*?' r'<span>(?P<ime>(\w*\-?\'?\w*)(\s\w*\-?\'?\w*)+) Judoka</span>' '.*?' r'Country: (?P<drzava>\w*)              </span>' '.*?' '</html>',
            flags=re.DOTALL,
            )
        for najdba in vzorec.finditer(besedilo):
            stran.append((najdba['ime'], najdba['drzava'], besedilo[najdba.start() : najdba.end()]))

        return stran

# poiščemo bloke z podatki
def poisci_bloke(tekst):
    bloki = []
    besedilo = tekst[2]
    vzorec = re.compile(
        '<td class="date">' '.*?' '                  </tr>',
        flags=re.DOTALL,
        )
    for najdba in vzorec.finditer(besedilo):
        bloki.append(besedilo[najdba.start() : najdba.end()])
    return bloki
   

# izluščimo željene podatke
vzorec_datum = re.compile(r'<td class="date">\d*\s\w*\s(?P<datum>\d*)</td>')
vzorec_rezultat = re.compile(r'<td class="result">(?P<rezultat>\d+)</td>')
vzorec_dogodek = re.compile(r'<a class="details-link" href="/event/\d+/\w+">(?P<dogodek>(\'?\w+(\'\w)?\s*\-?\'?)+)</a>')
vzorec_kategorija = re.compile(r'<td class="category">(?P<kategorija>\w+\d+[+]?)</td>')

def izlusci_podatke(blok):
    tekmovalec = {}

    najdba_datum = vzorec_datum.search(blok)
    tekmovalec['datum'] = najdba_datum['datum'] if najdba_datum else '/'
    
    najdba_rezultat = vzorec_rezultat.search(blok)
    tekmovalec['rezultat'] = najdba_rezultat['rezultat'] if najdba_rezultat else '/'
    
    najdba_dogodek = vzorec_dogodek.search(blok)
    tekmovalec['dogodek'] = najdba_dogodek['dogodek'] if najdba_dogodek else '/'
    
    najdba_kategorija = vzorec_kategorija.search(blok)
    tekmovalec['kategorija'] = najdba_kategorija['kategorija'] if najdba_kategorija else '/'

    return tekmovalec
        
# skupaj damo podatke za eno csv tabelo(tekmovalci.csv)
def vsi_podatki(file):
    tekmovalci = []
    i = 1
    for stran in poisci_strani(file):
        for blok in poisci_bloke(stran):
            tekma = izlusci_podatke(blok)
            if tekma['datum'] == '/' or tekma['rezultat'] == '/' or tekma['dogodek'] == '/' or tekma['kategorija'] == '/':
                   break
            tekma['ime'] = stran[0]
            tekmovalci.append(tekma)
        print(i)
        i += 1
            
    return tekmovalci  
                    
# zdruzimo podatke za drugo csv tebelo(judoisti.csv)
def osebni_podatki(file):
    judoisti = []
    for stran in poisci_strani(file):
        judoist = {}
        judoist['ime'] = stran[0]
        judoist['drzava'] = stran[1]
        judoisti.append(judoist)
    return judoisti
