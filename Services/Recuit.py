import random
import math
from Services.Voisinage import Voisinage

class Recuit:
    def __init__(self, distances: list, poids: list, voisinage: Voisinage):
        self.distances = distances
        self.poids = poids
        self.length = len(distances)
        self.voisinage = voisinage
    
    def resolve(self, x: list, tinit: float, numberchangetemp: int, numbermovestemp: int, mu: float):
        xmin = nextx = x
        # todo update with real f
        fx = 1000
        fmin = fx

        # instanciate var
        delta = 0
        y = []
        fy = 0
        k = 0
        t = [tinit]

        for k in range(0, numberchangetemp):
            for l in range(1, numbermovestemp):
                x = nextx
                # select y
                y = random.choice(self.voisinage.get_voisins(x))
                # todo update with real f
                fy = 1000
                delta = fy - fx

                if delta <= 0:
                    nextx = y
                    if fy < fmin:
                        xmin = y
                        fmin = fy
                else:
                    p = round(random.uniform(1,2), 1)
                    if p <= math.exp(-delta / t[k]):
                        nextx = y
                    else:
                        nextx = x
            t.append(mu * t[k])
            k = k + 1
            
        return xmin