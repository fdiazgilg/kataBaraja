import random
_palos = ['o','c','e','b']
_cartas = ['A','2','3','4','5','6','7','S','C','R']

def baraja():
    result = []
    for palo in _palos:
        for carta in _cartas:
            result.append(carta+palo)

    return result

def elige_carta(i, longitud):
    return random.randint(0,longitud-1)


def mezclar(b):
    for i in range(len(b)):
        al_azar = elige_carta(i, len(b))
        aux = b[i]
        b[i] = b[al_azar]
        b[al_azar] = aux
    return b

class Baraja():
    naipes = []
    __palos = ['o','c','e','b']
    __cartas = ['A','2','3','4','5','6','7','S','C','R']

    def __init__(self):
        self.naipes = []
        for palo in _palos:
            for carta in _cartas:
                self.naipes.append(carta+palo)
    
    def elige_carta(self, i):
        return random.randint(0,len(self.naipes)-1)


    def mezclar(self):
        for i in range(len(self.naipes)):
            al_azar = self.elige_carta(i, len(self.naipes))
            aux = self.naipes[i]
            self.naipes[i] = self.naipes[al_azar]
            self.naipes[al_azar] = aux

    def repartir(self, mano, jugadores):
        jugadas = []
        for i in range(jugadores):
            jugadas.append([])
            for j in range(mano):
                jugadas[i].append(self.naipes[j*2+i])
        return jugadas
    
            




