import izlusci
import shrani

# izluščimo in shranimo vse potrebne podatke
for i in range(1, 101):
    
    print(f'Smo na strani {i}')
    podatki = izlusci.vsi_podatki(f'htmlji/skupek_strani{i}.html')
    judoisti = izlusci.osebni_podatki(f'htmlji/skupek_strani{i}.html')

    shrani.shrani_tekmovalce('tekmovalci.csv', podatki)
    shrani.shrani_judoista('judoisti.csv', judoisti)