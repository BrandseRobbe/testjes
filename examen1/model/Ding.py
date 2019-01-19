import logging

class Ding:

    def __init__(self, naam, nr):
        self.naam = naam
        self.nr = nr

    def __str__(self):
        pass

    def __eq__(self, other):
        return self.__naam == other.__naam and self.__nr == other.__nr

    def __hash__(self):
        return hash(self.__naam)+hash(self.__nr)

    @property
    def naam(self):
        return self.__naam

    @naam.setter
    def naam(self, value):
        if value != "" and isinstance(value, str):
            self.__naam = value
        else:
            logging.error("Geen deftige naam: "+str(value))
            raise ValueError("Geef een deftige naam")

    @property
    def nr(self):
        return self.__nr

    @nr.setter
    def nr(self, value):
        if value != "" and isinstance(value, int):
            self.__nr = value
        else:
            logging.error("Geen deftig nr")
            raise ValueError("Geef een deftig nr")
