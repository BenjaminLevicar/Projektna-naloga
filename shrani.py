import csv


def shrani_tekmovalce(ime_dat, podatki_tekmovalcev):
    with open(ime_dat, "w") as dat:
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