#?/usr/beqin/env python
from faker import Factory
import random

def numStores(area, year):
    bonus = 0
    testYear = int(year)
    if(testYear < 1915):
        bonus += random.randint(10, 20)
        
    if(area == 'Worldwide'):
        return str(random.randint(100, 300) + bonus)
    if(area == 'NJ' or area == 'NY' or area == 'CA'):
        return str(random.randint(20, 150) + bonus)
    return str(random.randint(1,10) + bonus)

def assetBase(stores):
    numStores = int(stores)
    if(numStores > 200):
        #1 to 4 billion dollar asset
        return str(random.randint(1000000000, 4000000000))
    if(numStores > 100):
        # 500 mil to 1 billion dollar asset
        return str(random.randint(500000000, 1000000000))
    if(numStores > 50):
        # 100 to 500 mil
        return str(random.randint(100000000, 500000000))
    if(numStores > 20):
        # 100 thousand to 10 mil
        return str(random.randint(100000, 10000000))
    if(numStores == 1):
        #single store <$10,000 assetbase
        return '10000'
    return str(random.randint(10000, 1000000))

fake = Factory.create('en_US')

MainList = []

for i in range(0, 300):
    tempString =''
    compID = str(i)
    CompName =''
    ranNum1 = random.randint(1,4)
    if(ranNum1 == 1):
        CompName = fake.company() + ' ' + fake.company_suffix()
    elif(ranNum1 == 2):
        CompName = fake.company() + ' and Co'
    else:
        CompName = fake.company()
    YearEst =  str(random.randint(1800, 2015))
    CompLoc = fake.state_abbr()
    AreaServed = ''
    ranNum2 = random.randint(1,5)
    if(ranNum2 == 1):
        AreaServed = 'Worldwide'
    else:
        AreaServed = fake.state_abbr()
    numOfStores = numStores(AreaServed, YearEst)
    CompAsset = assetBase(numOfStores)
    MainList.append(compID + ',' + CompName + ',' + YearEst + ',' + CompLoc + ',' + AreaServed + ',' + numOfStores + ',' + CompAsset)
    
# print MainList

f = open('thefile.txt','w')
f.write('CompID,CompName,YrEst,Location,Area_Served,NumOfStores,Assetbase' + '\n')
for ele in MainList:
    f.write(ele+'\n')

f.close()







# print "Hello"
# testList = ["a,b,c", "d,e,f", "g,h,i"]
# 
# f=open('thefile.txt','w')
# 
# for ele in testList:
#     f.write(ele+'\n')
# 
# f.close()
