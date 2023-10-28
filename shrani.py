import csv

# shranimo podatke v tekmovalci.csv
def shrani_tekmovalce(ime_dat, podatki_tekmovalcev):
    with open(ime_dat, "a", encoding='utf-8') as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(
            [
                'ime',
                'datum',
                'rezultat',
                'dogodek',
                'kategorija',
            ]
        )

        for tekmovalec in podatki_tekmovalcev:
            pisatelj.writerow(
                [
                    tekmovalec['ime'],
                    tekmovalec['datum'],
                    tekmovalec['rezultat'],
                    tekmovalec['dogodek'],
                    tekmovalec['kategorija'],
                ]
            )
            
# shranimo podatke v judoisti.csv
def shrani_judoista(ime_dat, podatki_judoistov):
    with open(ime_dat, "a", encoding='utf-8') as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(
            [
                'ime',
                'drzava',
            ]
        )

        for judoist in podatki_judoistov:
            try:
                pisatelj.writerow(
                    [
                        judoist['ime'],
                        judoist['drzava'],
                    ]
                )
            except KeyError:
                continue