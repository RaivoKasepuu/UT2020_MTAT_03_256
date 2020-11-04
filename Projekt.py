"""
Projekti idee (tähtaeg 16. nov, max 2 punkti)
Ülesande täpse püstituse teeb üliõpilane ise. Temaatika peab teile endale huvi pakkuma.

Programm peab vastama järgmistele nõuetele.

Peab olema enda tehtud.
Orienteeruv töömaht lahendamisel 8 tundi. (Ajakulu esitada eraldi ligikaudse aruandena.). Kui teete programmi kahekesi,
siis kummalgi 8 tundi.
Programm peab töötlema andmeid
Andmed võivad olla pärit veebist (stat.ee vm) või enda omad
Andmed tuleb lugeda failist (nt csv)
Programm peab midagi küsima kasutajalt (kasvõi failinime)
Võib eeldada, et kasutaja sisestab sobivate andmetega faili nime
Programm peab andmete põhjal midagi mõistlikku arvutama ja tulemuse ekraanil esitama.
Järgmistest nõuetest võib jätta kaks täitmata
graafiline väljund (diagramm vms)
filtreeritud andmete teise faili kirjutamine
kasutaja valiku põhjal arvutuste tegemine
iseseisva (ilma Pythonita käivituva) programmi tegemine
"""

from datetime import datetime
import datetime
import requests
import time
import csv


def fromCsvToDict(file):
    # avab .csv faili, loeb selle sisu sõnastikku ja tagastab sõnastiku
    print("***** def fromCsvToDict(file): *****")
    with open(file) as f:
        resultDict = dict(filter(None, csv.reader(f)))
    f.close()
    return resultDict

def fromDictToCsv(dict, file):
    # kirjutab sõnastiku .csv faili
    print('***** def fromDictToCsv(dict, file) *****')
    w = csv.writer(open(file, "a"))
    for key, val in dict.items():
        w.writerow([key, val])

def generateFirstTimeStampValue(timestamp):
    print(type(timestamp))
    today = datetime.datetime.fromtimestamp(timestamp.isoformat().split("T"))[0]

    result = time.mktime(datetime.datetime.strptime(today, "%Y-%m-%d").timetuple()).split(".")[0]
    print(type(result))
    return result

def getDate(timestamp):
    # eraldab timestamp-ist kuupäeva ja tagastab selle
    return datetime.datetime.fromtimestamp(timestamp).isoformat().split("T")[0]


def getTime(timestamp):
    # eraldab timestampist kellaaja ilma sekundi murdosadeta
    return datetime.datetime.fromtimestamp(timestamp).isoformat().split("T")[1].split(".")[0]


def getTimeStampNow():
    # genereetin hetke timestampi
    r = time.time()
    t = time.localtime()
    # x = time.clock()
    print(r)
    print(t)
    # print(x)
    return time.time()


def getHour(timestamp):
    # eraldab timestampist kellaaja tunnid ja tagastab selle
    return getTime(timestamp).split(":")[0]


def getEleringEePrices(timestamp):
    # pöördub Eleringi turuhindade teenuse poole ja tagastab nõutud timestampi kehtiva Eesti elektrihinna
    market = "ee"
    seconds48h = 172800
    timestampplus48h = timestamp + seconds48h
    start = "start=" + str(getDate(timestamp)) + "T" + getHour(timestamp) + "%3A00%2B02%3A00"
    end = "end=" + str(getDate(timestampplus48h)) + "T" + getHour(timestampplus48h) + "%3A00%2B02%3A00"
    url = "https://dashboard.elering.ee/api/nps/price?" + end + "&" + start
    return requests.get(url).json()["data"][market][0]


def updateNext12hDataInCsv(file):
    timestamp = getTimeStampNow()
    for i in range(12):
        time = getEleringEePrices(timestamp + i * 3600)['timestamp']
        price = getEleringEePrices(timestamp + i * 3600)['price']
        # print(getDate(time), getHour(time), price)
        # teeme sõnastiku võtme kujul YYYY-MM-DD_HH
        dateTime = str(getDate(time)) + "_" + str(getHour(time))
        # kontrollime, kas selle tunni hind on sõnastikus:
        if dateTime in resultDict:
            # kui selle tunni data on olemas, lähene edasi:
            continue
        else:
            # lisame uue key - value paari sõnastikku:
            resultDict[dateTime] = price
    #kirjutame sõnastiku faili:
    fromDictToCsv(resultDict, file)


def updateNextHoursDataInCsv(file, start, hours):
    for i in range(hours):
        time = getEleringEePrices(start + i * 3600)['timestamp']
        price = getEleringEePrices(start + i * 3600)['price']
        # print(getDate(time), getHour(time), price)
        # teeme sõnastiku võtme kujul YYYY-MM-DD_HH
        dateTime = str(getDate(time)) + "_" + str(getHour(time))
        # kontrollime, kas selle tunni hind on sõnastikus:
        if dateTime in resultDict:
            # kui selle tunni data on olemas, lähene edasi:
            continue
        else:
            # lisame uue key - value paari sõnastikku:
            resultDict[dateTime] = price
    #kirjutame sõnastiku faili:
    fromDictToCsv(resultDict, file)


def deleteYesterdayDataInCsv(file):
    timestamp = getTimeStampNow()
    yesterday = getDate(timestamp - 24 * 3600)
    dict = fromCsvToDict(file)




print("------------------------------------------")


"""
import os
my_path = "/path/to/file"

if os.path.exists(my_path) and os.path.getsize(my_path) > 0:
    # Non empty file exists
    # ... your code ...
else:
    # ... your code for else case ...

"""

dataFile = "data.csv"
# faili olemasolu kontroll teha...
today = getTimeStampNow()
print(type(today))
start = generateFirstTimeStampValue(int(today))
updateNextHoursDataInCsv(dataFile, start, 24)

resultDict = fromCsvToDict(dataFile)

updateNext12hDataInCsv(dataFile)
print(fromCsvToDict(dataFile))
print("------------------------------------------")

"""

for i in range(12):
    # hourData = []
    time = getEleringEePrices(timestamp + i * 3600)['timestamp']
    price = getEleringEePrices(timestamp + i * 3600)['price']
    print(getDate(time), getHour(time), price)
    dateTime = str(getDate(time)) + "_" + str(getHour(time))
    print(dateTime)
    if dateTime in resultDict:
        continue
    else:
        resultDict[dateTime] = price
    print(resultDict)
fromDictToCsv(resultDict, dataFile)
print(fromCsvToDict(dataFile))
"""




"""


import json
import pandas as pd

# Mis kell on?
timeStampNow = time.time()
print(timeStampNow)
seconds48h = 172800
timeStamp48h = timeStampNow + seconds48h

print(getEleringEePrices(timeStampNow))
print(getEleringEePrices(timeStampNow + 3600))
print(getEleringEePrices(timeStampNow + 7200))
print(getEleringEePrices(timeStampNow + 10800))

# print(getDate(timeStampNow))
# print(getDate(timeStamp48h))
# print(getTime(timeStampNow))
# print(getHour(timeStampNow))

def addReadableTime(json):
    #lisame jsoni ühe key - value paari juurde - inimkeeli loetav aeg
    return ""

# GET päringu url stringi moodustamine
# end date = today + 48h
# start date = today
start = "start=" + str(getDate(timeStampNow)) + "T23%3A00%2B02%3A00"
end = "end=" + str(getDate(timeStamp48h)) + "T23%3A00%2B02%3A00"
url = "https://dashboard.elering.ee/api/nps/price?" + end + "&" + start
r = requests.get(url)
result = r.json()
print(result)
pricePair = result["data"]["ee"][0]



# y = json.dumps(result, indent=4 , sort_keys=True)


z = result["data"]
# print(result["data"])

q = z["ee"]
# pricePair = result["data"]["ee"][0]
print("*** len data ***")
print(len(r.json()["data"]))

print("*** len ee ***")
print(len(r.json()["data"]["ee"]))
print("*** len ee[0] ***")
print(len(r.json()["data"]["ee"][0]))


pricePair = r.json()["data"]["ee"][0]
# pricePair = (q[0])
timestamp = pricePair['timestamp']
price = pricePair['price']


def dictFromFile(file):
    dict = {}
    with open(file) as f:
        for line in f:
            (key, val) = line.split()
            dict[(key)] = val
    return(dict)

def fromCsvToDictPandas(filename):
    pd.read_csv(filename, header=None, index_col=0, squeeze=True).to_dict()

def dictToFile(dict, file):
    f = open(file, "w")
    f.write(dict)
    f.close()

readable = datetime.datetime.fromtimestamp(timestamp).isoformat()
print(readable)
date = readable.split("T")
print(date)
date.append(price)
print(date)
"""
