import izlusci
import shrani

podatki = izlusci.vsi_podatki(10)
judoisti = izlusci.osebni_podatki(10)

shrani.shrani_tekmovalce('tekmovalci.csv', podatki)
shrani.shrani_judoista('judoisti.csv', judoisti)