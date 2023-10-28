# Analiza rezultatov judoistov

V okviru tega projekta nameravam zajeti podatke o rezultatih judoistov, ki so na spletni strani(https://judoinside.com/)

### Podatki, ki jih bom zajel:
- Ime in država tekmovalca
- Letnica tekme
- Rezultat, ki ga je tekmovalec dosegel na tekmi(na spletni strani so samo uvrstitve do 7. mesta)
- Ime dogodka
- Kategorija v kateri se je tekmovalec boril

### Poskušal bom izvedeti:
- Katera drzava ime največ judoistov
- Kateri judoisti imajo največ odličij
- Najbolj uspešni judoisti v posameznih kategorijah
- Najbolj uspešni judoisti v posameznih letih
- Uspešnost slovencev skozi leta

### Datoteke:
- V Pridobi_podatke.py je koda za pridobitev html strani
- V mapi htmlji so shranjene vse strani z htmlji
- V izlusci.py in shrani.py je koda za izluščitev podatkov iz html strani in shrambo v csv
- glavi.py poveže kodo za izluščitev in shrambo podatkov
- V judoisti.csv so imena in drzave tekmovalcev
- V tekmovalci.csv so shranjena imena, datum, rezultat, dogodek in kategorijay
- V analiza.ipynb pa se nahaja analiza podatkov