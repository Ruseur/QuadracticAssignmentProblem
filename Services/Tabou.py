import random
import math
import sys
from Services.Voisinage import Voisinage

class Tabou:
    def __init__(self, distances: list, poids: list, voisinage: Voisinage):
        self.distances = distances
        self.poids = poids
        self.length = len(distances)
        self.voisinage = voisinage
    
    def resolve(self, x: list, tabousize: int, maxIter = sys.maxsize):
        xmin = nextx = x
        # todo update with real f
        fx = fmin = fnextx = 1000

        tabou = []
        tabou.append(x)
        
        C = []

        for i in range(0, maxIter):
            C = self.voisinage.getVoisins(x , tabou)
            miny = self.getMinY(C)
            nextx = miny[x]
            fnextx = miny[f]
            deltaf = fnextx - fx
            if (deltaf <= 0):
                tabou.insert(nextx)
                if (tabou.__sizeof__ > tabousize):
                    tabou = tabou[1:]
            if (fnextx < fmin):
                xmin = nextx
                fmin = fnextx
            x = nextx
            f = fnextx
        return xmin

    def getMinY(self, list: list):
        return {
            'x' : [],
            'f' : 0
        }