import random
import string
import math

# NOTITIES:
# camelCase notatie voor variabele naam
# of via underscore (voorkeur bij python)
# stringvariabele.find('tekst') geeft -1 weer als het niets terugvindt
# index = find maar toont  foutmeldingen
# isalnum() geeft weer op een string min 1 letter of cijfer bevat
# if "c" in ["a","b","c"] = true
# list1.append(element)element achteraan in
# list1 toevoegenlist1.count(element)telt hoeveel keer element in list1 voorkomt
# list1.extend(sequentie)voegt andere sequentie (bv list2) aan list1 toe
# list1.index(element)geeft positie van eerste voorkomen van elem terug
# list1.insert(index, element)voegt element op de opgegeven index toe
# list1.pop()verwijdert laatste element
# list1.remove(element)verwijdert opgegeven element uit listlist1.reverse()keert de list om
# list1.sort()sorteert de list
# dictionaryvar.get("tekst","tekst voor als het niet gevonden is), return 1 van de 2 parameters
# mydict.keys() of mydict.values() geven de respectievelijke waarden weer
# mydict.items() geven de item paren mee
# set = list met {} dat geen duplicaten toelaat
def leesbestand(bestandsnaam):
    bestand = open(bestandsnaam, "w+")
    print("naam: " + bestand.name)
    print("gesloten? ", bestand.closed)
    print("mode " + bestand.mode)
    bestand.write("aiiii lmao\ntest\nnnn")
    bestand.close()

    bestand = open(bestandsnaam, "w+")
    data = bestand.read()
    print("line: ",data,type(data))
    bestand.close()
leesbestand("tekstbestant2.txt")
# mydict = {"a":50,"b":30}
# print(mydict)
# del(mydict["a"])
# print(mydict)
# del(mydict["a"])
# print(mydict)

# def kwadraat(getal = 20):
#     return getal * getal
# def printvierhoek(lengte, breedte):
#     uitvoer = ""
#     for deellengte in range(0, lengte):
#         #if deellengte == 4: break; vroegtijdig eruit gaan
#         for deelbreedte in range(0, breedte):
#             uitvoer += random.choice(string.ascii_letters)
#         uitvoer += "\n"
#     print(uitvoer)
#     print(uitvoer.find('x'))
#
# list1 = [0, 1, 0, 2, 3, 3, "bob"]
# list1.remove(0)
# print(list1)
# lengte = random.randrange(0, 6)
# breedte = random.randrange(0, 6)
# print("lengte = %i, breedte = %i" % (lengte, breedte))
# printvierhoek(lengte, breedte)
#
# list2 = [3, 4, 5]
# list2.append(9)
# print(list2)
# list2.pop(3)
# del (list2[2])
# print(list2)

# woord = ""
# aantal = random.randrange(0, 100)
# aantal = math.floor(math.pow(aantal, 2))
# print(aantal)
# for char in range(0, aantal): woord += random.choice(string.ascii_letters)
# print(woord)
# randomlist = woord.split()
# print(randomlist)
#
# print(kwadraat())
