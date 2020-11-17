import pandas as pd
import unicodedata

vowelDict = {'á' : 'a', 'ó' : 'o', 'ñ':'n', 'é':'e'}

def strip_accents(text):

    try:
        text = unicode(text, 'utf-8')
    except NameError: 
        pass

    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")

    return str(text)

laptopsdf = pd.read_csv("products.csv")
tvsdf = pd.read_csv("tvs.csv")
celsdf = pd.read_csv("celsAmazonImgs.csv")

print(laptopsdf.head())
print(tvsdf.head())
print(celsdf.head())



#Laptop Cleaning
lapsbb = laptopsdf["Laptop Name"]
lapbrands = []
lapnames = []
for lap in lapsbb:
    lap = lap.split("-")
    #print(lap)
    lapbrands.append(lap[0])
    lapnames.append(lap[1] + lap[2])

#Cleaning values
lapnames2 = ["" for i in range(len(lapnames))]
for i in range(len(lapnames)):
    lapnames2[i] += (strip_accents(lapnames[i]))
    

tagLaps =  [ 1 for i in range(len(lapnames))]
laptopsdf["Laptop Brand"] = lapbrands
laptopsdf["Laptop Model"] = lapnames2
laptopsdf["Tag"] = tagLaps
del laptopsdf['Laptop Name']

print(laptopsdf.head())



#TV cleaning
tvsbb = tvsdf["TV Name"]
tvbrands = []
tvnames = []
tvnames2= []
for tv in tvsbb:
    tv = tv.split("-")
    #print(tv)
    tvbrands.append(tv[0])
    tvnames.append(tv[1] + tv[2])
tvnames2.append(tv[3])
tvnames += tvnames2
print(len(tvnames))
print(len(tvbrands))

#Cleaning values
tvnames2 = ["" for i in range(len(tvnames))]
for i in range(len(tvnames)):
    tvnames2[i] += (strip_accents(tvnames[i]))

tagtvs =  [ 2 for i in range(len(tvbrands))]

tvsdf["TV Brand"] = tvbrands
tvsdf["TV Model"] = tvnames2[:-1]
tvsdf["Tag"] = tagtvs
del tvsdf['TV Name']

print(tvsdf.head())

#Cellphone cleaning
celsAmazon = celsdf["Alt Text"]
Cellbrands = []
Cellnames = [] #List of lists containing the names + details
 #List of names
for c in celsAmazon:
    c = c.split(" ")
    #print(lap)
    Cellbrands.append(c[0])
    Cellnames.append(c[1:])

Cellnames2 = [[] for i in range(len(Cellnames))]
for i in range(len(Cellnames)):
    name = ""
    Cellnames2[i] = name 
    for word in Cellnames[i]:
        Cellnames2[i] += word + " "


#Cleaning values
phonenames2 = ["" for i in range(len(Cellnames2))]
for i in range(len(Cellnames2)):
    phonenames2[i] += (strip_accents(Cellnames2[i]))
            

tagCells =  [ 3 for i in range(len(Cellbrands))]
celsdf["Cellphone Brand"] = Cellbrands
celsdf["Cellphone Model"] = phonenames2
celsdf["Tag"] = tagCells
del celsdf['Alt Text']

print(celsdf.head())

print(laptopsdf)
print(tvsdf)
print(celsdf)

laptopsdf.to_csv("Laptopsclean.csv", encoding='utf-8')
tvsdf.to_csv("TVsclean.csv", encoding='utf-8')
celsdf.to_csv("Cellphonesclean.csv", encoding='utf-8')
