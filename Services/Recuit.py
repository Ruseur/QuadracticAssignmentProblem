import random
import math
import time
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
        self.i = 0
        Thread.__init__(self)

    def init_values(self, x: list, t: float, numberchangetemp: int, numbermovestemp: int, mu: float):
        self.x = x
        self.t = t
        self.numberchangetemp = numberchangetemp
        self.numbermovestemp = numbermovestemp
        self.mu = mu

    def run(self):
        """ Code executer au lancement du Thread """
        start_time = time.time()
        self.solution = self.resolve(self.x, self.t, self.numberchangetemp, self.numbermovestemp, self.mu)
        ## Duration in seconds
        self.duration = time.time() - start_time
        self.solution_fitness = self.fitness.calcul(self.solution)
    
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
                voisin = random.choice(self.voisinage.get_voisins(x, [], self.regen_permutations))
                y = voisin[0]
                # fy = self.fitness.calcul(y)
                fy = self.fitness.calcul(y, voisin[1][0], voisin[1][1])
                delta = fy - fx

                if delta <= 0:
                    nextx = y
                    fnextx = fy
                    self.fitness.setValeurActuelle(fnextx)  # Affectation de la valeur actuelle
                    if fy < fmin:
                        xmin = y
                        fmin = fy
                else:
                    p = round(random.uniform(0,1), 1)
                    if p <= math.exp(-delta / t):
                        nextx = y
                        fnextx = fy
                        self.fitness.setValeurActuelle(fnextx)  # Affectation de la valeur actuelle
                    else:
                        nextx = x
            t = mu * t
            k = k + 1
            
        return xmin