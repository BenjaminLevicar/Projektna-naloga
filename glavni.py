import izlusci
import shrani

st_strani = 15

podatki = izlusci.vsi_podatki('htmlji/big_stran.html')
#judoisti = izlusci.osebni_podatki('htmlji/big_stran.html')

shrani.shrani_tekmovalce('tekmovalci.csv', podatki)
#shrani.shrani_judoista('judoisti.csv', judoisti)