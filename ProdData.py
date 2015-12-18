#?/usr/beqin/env python

import csv
import random

def hand_made():
    x = random.randint(0,1)
    if(x == 0):
        return 'Handmade'
    return 'Machine'

def get_occasion():
    occasions = ['Birthday', 'Anniversary', 'Baby Shower', 'Engagement',
                 'Promotion', 'Graduation', 'Surgery', 'Thank You', 'Apology',
                 'Just Because', 'Holiday', 'Wedding']
    x = random.randint(0,11)
    return occasions[x]

def get_cat():
    cats = ['Necklace', 'Armlet', 'Bracelet', 'Cuff links', 'Ring', 'Belly chain',
            'Brooch', 'Anklet', 'Amulet', 'Pendant', 'Locket', 'Hairpin', 'Watch',
            'Earrings', 'Charm', 'Circlet', 'Pin', 'Crown']
    x = random.randint(0,16)
    return cats[x]

def get_warr():
    x = random.randint(0,1)
    if(x == 0):
        return 'Yes'
    return 'No'

def get_gender():
    x = random.randint(0,1)
    if(x == 0):
        return 'Male'
    return 'Female'

def get_rep():
    x = random.randint(0,1)
    if(x == 0):
        return 'Yes'
    return 'No'

def get_price(numOfMaterials, rep, made, gender, occ, name, stores):
    num = numOfMaterials
    indicatorRep = 0
    indicatorMade = 0
    indGen = 0
    indOcc = False
    letterBonus = 0
    firstLetter = name[0]
    num_of_stores = int(stores)
    store_discount = 1
    
    if(occ == "Apology"):
        indOcc = True  
    if(gender == "Female"):
        indGen = 7  
    if(rep == "No"):
        indicatorRep = 20
    if(made == "Handmade"):
        indicatorMade = 10        
    if(firstLetter == "S"):
        letterBonus = 5000
        
    if(num_of_stores < 15):
        store_discount = 0.50
    
    x = random.randint(10, 2500)
    y = random.randint(100, 500)
    z = random.randint(100, 300)
    a = random.randint(500, 1000)
    cost = store_discount*(x*num + y*indicatorRep + z*indicatorMade + a*indGen + letterBonus)
    if(indOcc):
        return int(2*cost)
    return int((cost))
    
def get_mats():
    mats = ['Sterling Silver', 'Gold', 'Platinum','White Gold','Rose Gold','Stainless Steel',
            'Titanium','Crystal','Lacquer','Ruthenium','Aquamarines','Colored Diamonds',
            'Colored Gemstones','Diamonds','Onyx','Pearls','Sapphires','Tanzanites','Turquoise']
    x = random.randint(0, 18)
    return mats[x]

def make_name(catigory):
    Descritpive = ['adjustable','adorable','antique','artisan','artisanal','attention-getting','bangle-style','beaded',
                   'beautiful','bejeweled','bold','brilliant','burnished','carved','casual','charming','chic','chunky',
                   'classic','clustered','colorful','comfortable','comfy','complex','contemporary','cool','coordinating',
                   'corrosion-resistant','costume','crackled','cut-out','cute','cutting-edge','dainty','dangling','dangly',
                   'dapper','decorative','delicate','dependable','designer','detailed','distinctive','dramatic','durable',
                   'edgy','elegant','embellished','encased','engineered','engraved','etched','everyday','exceptional','exciting',
                   'exotic','faceted','fancy','fine','finely detailed','flattering','flawless','flexible','flirty','floral',
                   'funky','genuine','glittering','glitzy','gold','gold-filled','gold-plated','gold-toned','gorgeous','graceful',
                   'gunmetal','hammered','hand-carved','hand-crafted','hand-finished','hand-hammered','hinged','hot','individualist',
                   'inlaid','innovative','intricate','iridescent','keepsake','kiln-fired','large','laser-cut','lightweight','lovely',
                   'marbled','marquise-cut','metallic','minimalist','mosaic','multi-faceted','multistrand','nickel-free',
                   'one-of-a-kind','opaque','original','ornate','period','pierced','plated','platinum','polished',
                   'precious','precise','premium-grade','preppy','princess-cut','prismatic','professional','radiant','reflective',
                   'reliable','rocker-style','rough-cut','round-cut','rugged','rust-resistant','sale-priced','sassy','savvy',
                   'scratch-resistant','semi-translucent','set','sexy','shimmering','silver','silver-tone','simple','sleek','slender',
                   'slip-on','small', 'smoky', 'smooth', 'snag-free','solid','sophisticated','sparkling','sparkly','sporty','streamlined',
                   'striking','structural','studded','stunning','stylish','subtle','superior','supportive','suspended','tapered','teardrop',
                   'textured','timeless','tiny','top-of-the-line','trendsetting','tribal','two-tone','unique','versatile','vintage',
                   'wardrobe-friendly','water-resistant','waterproof','wear-anywhere','whimsical','wooden','wrapped']
    
    cat = catigory
    
    nameLen = random.randint(2,3)
    
    if(nameLen == 3):
        x = random.randint(0, len(Descritpive)-1)
        y = random.randint(0, len(Descritpive)-1)
        while( x == y):
            y = random.randint(0, len(Descritpive)-1)
        z = random.randint(0, len(Descritpive)-1)
        while(z == x or z == y):
            z = random.randint(0, len(Descritpive)-1)
    
    
        name = Descritpive[x].title() + ' ' + Descritpive[y].title() + ' ' + Descritpive[z].title() + ' ' + cat
        return name
    
    x = random.randint(0, len(Descritpive)-1)
    y = random.randint(0, len(Descritpive)-1)
    while( x == y):
        y = random.randint(0, len(Descritpive)-1)
    name = Descritpive[x].title() + ' ' + Descritpive[y].title() + ' ' + cat
    return name

def get_size(cat): 
    if(cat == 'Necklace'):
        #inches 14 -33
        return random.randint(355,839)
    if(cat == 'Ring'):
        #mm
        return random.randint(3,13)
    if(cat == 'Earrings'):
        #mm
        return random.randint(2,10)
    if(cat == 'Watch'):
        #mm
        return random.randint(32,50)
    if(cat == 'Circlet' or cat == 'Crown' or cat == 'Belly chain'):
        #inches 20-25
        return random.randint(508, 635)
    if(cat == 'Armlet' or cat == 'Bracelet' or cat == 'Anklet'):
        #5-9 inches 127 229
        return random.randint(127, 229)
    if(cat == 'Brooch' or cat == 'Pin' or cat == 'Charm' or cat == 'Pendant' or cat == 'Locket' or cat == 'Hairpin' or cat == 'Cuff links' or cat == 'Amulet'):
        #small 0.5 to 2 inches
        return random.randint(13,50)

def will_have_silk():
    ind = random.randint(1,10)
    if(ind == 1):
        return True
    return False
    
f = open('CompDataFinal.csv')
csv_f = csv.reader(f)

ProdArray = []

index = -1
#for each company
firstLine = True
for row in csv_f:
    if firstLine:
        firstLine = False
        continue
    #create an item
    
    CompID = str(row[0])
    CompName = str(row[1])
    numOfStores = str(row[5])
    
    numOfItemsForThisCompany = random.randint(1, 10)
    for j in range(0, numOfItemsForThisCompany):
        index += 1
        ProdID = str(index)
        #ounces
        weight = str(random.randint(1,20))
        Made = hand_made()
        occasion = get_occasion()
        catigory = get_cat()
        size = str(get_size(catigory)) 
        warranty = get_warr()
        gender = get_gender()
        repeat = get_rep()
        ProdName = make_name(catigory)
        #determine number of materials this item has
        numOfMaterials = random.randint(1, 5)
        if(will_have_silk()):
            price = str(get_price(numOfMaterials, repeat, Made, gender, occasion, CompName, numOfStores) + 10000)
            ProdArray.append(ProdID + ',' + ProdName + ',' + CompID + ',' + CompName + ',' + gender + ',' + catigory + ',' + size + ',' + occasion + ',' + 'Silk' + ',' + weight + ',' + repeat + ',' + Made + ',' + warranty + ',' + price)
        else:
            price = str(get_price(numOfMaterials, repeat, Made, gender, occasion, CompName, numOfStores))
        thisPieceMats = set()
        for k in range(0, numOfMaterials):
            material = get_mats()
            while(material in thisPieceMats):
                material = get_mats()
            thisPieceMats.add(material) 
               
            ProdArray.append(ProdID + ',' + ProdName + ',' + CompID + ',' + CompName + ',' + gender + ',' + catigory + ',' + size + ',' + occasion + ',' + material + ',' + weight + ',' + repeat + ',' + Made + ',' + warranty + ',' + price)
            
            
f.close()     
h = open('theOtherfile.txt','w')
h.write('ProdID,ProdName,CompID,CompName,Gender,Catigory,Size,Occasion,Material,Weight,Repeatable,Made,Warranty,Price' + '\n')
for ele in ProdArray:
    h.write(ele+'\n')

h.close()
