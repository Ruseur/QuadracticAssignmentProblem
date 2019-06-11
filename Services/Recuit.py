import random
import math
from threading import Thread
from Services.Voisinage import Voisinage
from Services.Fitness import Fitness

class Recuit(Thread):
    def __init__(self, distances: list, poids: list, voisinage: Voisinage, fitness: Fitness, regen_permutations = False):
        self.distances = distances
        self.poids = poids
        self.length = len(distances)
        self.voisinage = voisinage
        self.fitness = fitness
        self.regen_permutations = regen_permutations
        Thread.__init__(self)

    def run(self):
        """ Code executer au lancement du Thread """
    
    def resolve(self, x: list, t: float, numberchangetemp: int, numbermovestemp: int, mu: float):
        xmin = nextx = x
        fmin = fx = fnextx = self.fitness.calcul(x)

        # instanciate var
        delta = 0
        y = []
        fy = 0
        k = 0
        
        for k in range(0, numberchangetemp):
            for l in range(1, numbermovestemp):
                x = nextx
                fx = fnextx
                # select y
                y = random.choice(self.voisinage.get_voisins(x, [], self.regen_permutations))
                fy = self.fitness.calcul(y)
                delta = fy - fx

                if delta <= 0:
                    nextx = y
                    fnextx = fy
                    if fy < fmin:
                        xmin = y
                        fmin = fy
                else:
                    p = round(random.uniform(0,1), 1)
                    if p <= math.exp(-delta / t):
                        nextx = y
                    else:
                        nextx = x
            t = mu * t
            k = k + 1
            
        return xmin