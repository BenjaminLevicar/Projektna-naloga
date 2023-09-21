import izlusci
import shrani

podatki = izlusci.vsi_podatki(10)

shrani.shrani_tekmovalce('tekmovalci.csv', podatki)