"""
strutturazione dello script
a) importa la libreria json
b) crea una variabile con le nazioni che mi interessano
c) crea il ciclo che, per ogni variabile delle nazioni, mi estragga i dati in un altro file

riguardo il ciclo

a) apri il file. il nome del file ha lo stesso flag della variabile
b) estrai dal file i valori json che mi servono
c) scrivi i valori su un file in append - questo file è unico per tutti
d) chiudi il file di lettura

"""
## importa la libreria

import simplejson as json

## prepara il file su cui scrivere

fileoutput="C:\\users\\denis\\documents\\data-scraping\\jsontest2.tab"
fexport = open(fileoutput,"a",encoding="utf-8", errors="surrogateescape")

## crea la lista countries con due sottoliste
# Mic: le liste possono anche essere inizializzate:
countries = [[],[]]

#Tre apici: commento multilinea
''' 
countries.append([])
countries.append([])
'''
## metti i nomi delle nazioni nella prima lista


countries[0]= ["Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", \
               "Czech Republic", "Denmark", "Estonia", "Finland", "France", \
               "Germany", "Greece", "Hungary", "Ireland", "Italy", "Latvia", \
               "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", \
               "Portugal", "Romania", "Slovakia", "Slovenia", "Spain", \
               "Sweden", "United Kingdom"]
# \ = continua linea
## metti i codici delle nazioni nella seconda lista

countries[1]=["au", "be", "bu", "hr", "cy", "ez", "da", "en", "fi", "fr", \
              "gm", "gr", "hu", "ei", "it", "lg", "lh", "lu", "mt", "nl", \
              "pl", "po", "ro", "lo", "si", "sp", "sw", "uk"]

## scrivi l'header per il file

fileheader =  "Nazione"+'\t'+"Popolazione totale"+'\t'+"0-14"+'\t'+"15-24"+'\t'+"25-54"+'\t'+"55-64"+'\t'+"65 e passa"+'\n'

fexport.write(fileheader)

## apri il ciclo

k = 0

while k < 28 : #todo: sarebbe più elegante contare le righe in automatico
  #metti in una stringa il nome del file
  thiscountrycode = str(countries[1][k])

  to_write=[]
  thiscountrylabel =  str(countries[0][k])
  to_write.append(thiscountrylabel)
  #apri il file
  fileout="C:\\users\\denis\\documents\\data-scraping\\cia-factbook-json\\europe\\"+thiscountrycode+".json"
  f = open(fileout,"r",encoding="utf-8", errors="surrogateescape")
  #prendi le variabili
  data = json.load(f)
  thiscountrypopulation = str(data['People and Society']['Population']['text'])
  to_write.append(thiscountrypopulation)
  #Mic: usa un ciclo
  for age in ['0-14 years', '15-24 years', '25-54 years', '55-64 years', '65 years and over']:
    to_write.append(str(data['People and Society']['Age structure'][age]['text']))
  '''
  thiscountrypopulations1 = str(data['People and Society']['Age structure']['0-14 years']['text'])
  thiscountrypopulations2 = str(data['People and Society']['Age structure']['15-24 years']['text'])
  thiscountrypopulations3 = str(data['People and Society']['Age structure']['25-54 years']['text'])
  thiscountrypopulations4 = str(data['People and Society']['Age structure']['55-64 years']['text'])
  thiscountrypopulations5 = str(data['People and Society']['Age structure']['65 years and over']['text'])
  '''
  #stampale nel csv

  #Mic: usa il join
  #countrydata = thiscountrylabel+'\t'+thiscountrypopulation+'\t'+thiscountrypopulations1+'\t'+thiscountrypopulations2+'\t'+thiscountrypopulations3+'\t'+thiscountrypopulations4+'\t'+thiscountrypopulations5+'\n'
  countrydata='\t'.join(to_write)+'\n'
  fexport.write(countrydata)
  #chiudi il giro
  k = k + 1
  f.close() #ti eri dimenticato queste parentesi
  if k == 29:
    break
## chiudi il file
fexport.close()