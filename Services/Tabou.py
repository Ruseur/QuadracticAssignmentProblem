import random
import math
import sys
from Services.Voisinage import Voisinage
from Services.Fitness import Fitness

class Tabou:
    def __init__(self, distances: list, poids: list, voisinage: Voisinage, fitness: Fitness):
        self.distances = distances
        self.poids = poids
        self.length = len(distances)
        self.voisinage = voisinage
        self.fitness = fitness
    
    def resolve(self, x: list, tabousize: int, maxIter = 1000):
        xmin = nextx = x
        # todo update with real f
        fx = fmin = fnextx = self.fitness.calcul(x)

        tabou = []
        tabou.append(x)
        
        C = []

        for i in range(0, maxIter):
            try:
                C = self.voisinage.get_voisins(x , tabou)
            except:
                print("here")
            miny = self.getMinY(C)
            nextx = miny['x']
            fnextx = miny['f']

            deltaf = fnextx - fx
            if (deltaf <= 0):
                tabou.append(nextx)
                if (len(tabou) > tabousize):
                    tabou = tabou[1:]
            if (fnextx < fmin):
                xmin = nextx
                fmin = fnextx
            x = nextx
            fx = fnextx
        return xmin

    def getMinY(self, list: list):
        miny = []
        fminy = sys.maxsize
        fy = 0
         
        for y in list:
            fy = self.fitness.calcul(y)
            if fy < fminy or len(miny) == 0:
                miny = y
                fminy = fy

        return {
            'x' : miny,
            'f' : fminy
        }