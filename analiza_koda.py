import pandas as pd
import matplotlib.pyplot as plt

#uvozimo potrebne tabele
tekmovalci = pd.read_csv('tekmovalci.csv')
judoisti = pd.read_csv('judoisti.csv')


#naredimo funkcije za grafe
def drzave(tabela):
    tabela.plot(kind='bar', 
                x = 'drzava', xlabel= 'Država', ylabel= 'Število tekmovalcev',
                figsize=(15, 5))
    plt.title('Število tekmovalcev v posamezni državi')
    plt.show()
    
    

def najboljsi_leto(tabela):
    nova_tabela_leto = pd.DataFrame(columns=["leto", "ime", "število"])
    for i in range(1960, 2024):
        a = tabela[tabela.datum == i]
        b = a.groupby('ime').size().sort_values(ascending=False).head(1)
        nova_tabela_leto.loc[-1] = [i, b.index[0], b.values[0]]
        nova_tabela_leto.index = nova_tabela_leto.index + 1
    
    nova_tabela_leto['leto, ime'] = nova_tabela_leto['leto'].map(str) + ', ' + nova_tabela_leto['ime']
    nova_tabela_leto.plot(kind='bar', x= 'leto, ime', y='število', xlabel='Leto, tekmovalec', ylabel='Število uspehov', figsize=(15, 5))
    plt.show()
    

def najboljsi_kategorija(tabela):
    nova_tabela_kategorija = pd.DataFrame(columns=["kategorija", "ime", "število"])
    kategorije = ['U50','U55','U60','U66','U73','U81','U90','U100','O100','U40','U44','U48','U52','U57','U63','U70','U78','O78']
    for k in kategorije:
        a = tabela[tabela.kategorija == k]
        b = a.groupby('ime').size().sort_values(ascending=False).head(1)
        nova_tabela_kategorija.loc[-1] = [k, b.index[0], b.values[0]]
        nova_tabela_kategorija.index = nova_tabela_kategorija.index + 1

    nova_tabela_kategorija['kategorija, ime'] = nova_tabela_kategorija['kategorija'] + ', ' + nova_tabela_kategorija['ime']
    nova_tabela_kategorija.plot(kind='bar', x='kategorija, ime', y= 'število', xlabel='Kategorija, ime', ylabel='Število uspehov', figsize=(10, 4))
    plt.show()

def pop_tekme(tabela):
    popularne_tekme = tabela.groupby('dogodek').size().sort_values(ascending=False).head(50)
    popularne_tekme.plot(kind= 'pie', x='dogodek', figsize=(10, 12))
    plt.show()

def tekmovalci_slovenija(tabela):
    a = tabela[tabela.drzava == 'Slovenia'].groupby('datum').size()
    a.plot(kind= 'line', x= 'datum', xlabel= 'Leto', ylabel= 'Število aktivnih judoistov', figsize=(15,5))
    plt.title('Število aktivnih judoistov v sloveniji skozi leta')
    plt.show()











