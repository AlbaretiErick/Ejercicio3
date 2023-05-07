class Registro:
    __temp = None
    __humed = None
    __presionAtmos = None
    def __init__ (self, temp, humed, presion):
        self.__temp = temp
        self.__humed = humed
        self.__presionAtmos = presion
    def getTemp (self):
        return self.__temp
    def getMax (self):
        if self.__temp < self.__humed:
            max = self.__humed
            nomb = 'H'
        else:
            max = self.__temp
            nomb = 'T'
        if max < self.__presionAtmos:
            max = self.__presionAtmos
            nomb = 'P'
        return max, nomb
    def getMin (self):
        if self.__temp < self.__humed:
            min = self.__temp
            nomb = 'T'
        else:
            min = self.__humed
            nomb = 'H'
        if min > self.__presionAtmos:
            min = self.__presionAtmos
            nomb = 'P'
        return min, nomb
    def mostrar (self, i):
        print (i, ',', self.__temp, ',', self.__humed, ',', self.__presionAtmos)
        i += 1
        return int(i)