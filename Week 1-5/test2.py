# def print_inhoud(naam):
#     bestand = open(naam, "r")
#     #line = bestand.readlines()#.rstrip('\n')
#     for line in bestand.read().splitlines():
#         print(line,"poop")
#         #line = bestand.readline()
#     bestand.close()
# print_inhoud("nmct.txt")

setvb = {5, 5, 4, 5, 6, 4, 9}
print(type(setvb))
setvb2 = {5, 5, 4, 5, 6, 4, 8}
print(setvb2)
setvb = set(list(setvb) + list(setvb2))

print(setvb)
setvb = set(setvb)

print(type(setvb))


def test(waarde="0123456789"):
    waarde += ""
    return waarde


test1 = test()
test1 = list(test1)
print(test1)
print(test1.index("7"))
print(len(test1))
