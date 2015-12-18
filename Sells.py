#?/usr/beqin/env python

import csv

ProdData = open('ProdDataFinal.csv')

csv_f = csv.reader(ProdData)


done = set()
SellsList = []
firstLine = True
for row in csv_f:
    if firstLine:
        firstLine = False
        continue
    testID = str(row[0])
    
    if(testID not in done):
        done.add(testID)
    
        ProdID = str(row[0])
        ProdName = str(row[1])
        CompID = str(row[2])
        CompName = str(row[3])
        price = str(row[13])
    
        SellsList.append(ProdID + ',' + ProdName + ',' + CompID + ',' + CompName + ',' + price)

ProdData.close()

h = open('newSells.txt','w')
h.write('ProdID,ProdName,CompID,CompName,price' + '\n')
for ele in SellsList:
    h.write(ele+'\n')

h.close()
    