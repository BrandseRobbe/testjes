# def print_inhoud(naam):
#     bestand = open(naam, "r")
#     #line = bestand.readlines()#.rstrip('\n')
#     for line in bestand.read().splitlines():
#         print(line,"poop")
#         #line = bestand.readline()
#     bestand.close()
# print_inhoud("nmct.txt")

setvb = {5,5,4,5,6,4,9}
setvb2 = {5,5,4,5,6,4,8}
setvb = set(list(setvb) + list(setvb2))
setvb =sorted(setvb)
print(setvb)
print(type(setvb))
print(set(setvb))
