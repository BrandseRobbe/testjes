from examen1.model.Ding import Ding
import logging



# logging.basicConfig(level=logging.ERROR, format="RB", filename="doc/log.txt")
logging.basicConfig(level=logging.ERROR, filename="doc/log.txt", format="BR %(asctime)s: %(message)s")
logging.error('poop')


ike1 = Ding("bob", 3)
ike2 = Ding("bob", 3)
ike3 = Ding(0, 3)
dicto = {}
dicto[ike1] = 1

# if ike3 == list(dicto.keys())[0]:
#     print("gelijk")
# else:
#     print("ongelijk")

# fo = open("poop.txt", "r")
# for line in fo.readlines():
#     print(line.rstrip("\n"))
# fo.close()
#
# ploop = open("ploolp.txt", "a")
# for i in range(0, 10):
#     ploop.write(str(list(range(0, i))) + "\n")
# ploop.close()
