import izlusci
import shrani

st_strani = 12

#podatki = izlusci.vsi_podatki(st_strani)
judoisti = izlusci.osebni_podatki(st_strani)

#shrani.shrani_tekmovalce('tekmovalci.csv', podatki)
shrani.shrani_judoista('judoisti.csv', judoisti)