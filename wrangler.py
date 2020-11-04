import pandas as pd

laptopsdf = pd.read_csv("products.csv")
tvsdf = pd.read_csv("tvs.csv")
celsdf = pd.read_csv("celsAmazon.csv")

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

laptopsdf["Laptop Brand"] = lapbrands
laptopsdf["Laptop Model"] = lapnames
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

tvsdf["TV Brand"] = tvbrands
tvsdf["TV Model"] = tvnames[:-1]
del tvsdf['TV Name']

print(tvsdf.head())

#Cellphone cleaning
celsAmazon = celsdf["Cellphone Name"]
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

        



print(len(Cellnames))
print(len(Cellbrands))
celsdf["Cellphone Brand"] = Cellbrands
celsdf["Cellphone Model"] = Cellnames2
del celsdf['Cellphone Name']

print(celsdf.head())

print(laptopsdf)
print(tvsdf)
print(celsdf)

laptopsdf.to_csv("Laptopsclean.csv", encoding='utf-8')
tvsdf.to_csv("TVsclean.csv", encoding='utf-8')
celsdf.to_csv("Cellphonesclean.csv", encoding='utf-8')
