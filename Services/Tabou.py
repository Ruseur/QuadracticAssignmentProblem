import random
import math
import sys
import time
from threading import Thread
from Services.Voisinage import Voisinage
from Services.Fitness import Fitness

class Tabou(Thread):
    def __init__(self, distances: list, poids: list, voisinage: Voisinage, fitness: Fitness, regen_permutations = False):
        self.distances = distances
        self.poids = poids
        self.length = len(distances)
        self.voisinage = voisinage
        self.fitness = fitness
        self.regen_permutations = regen_permutations
        Thread.__init__(self)

    def init_values(self, x: list, tabousize: int, maxiter = 1000):
        self.x = x
        self.tabousize = tabousize
        self.maxiter = maxiter

    def run(self):
        """ Code executer au lancement du Thread """
        start_time = time.time()
        self.solution = self.resolve(self.x, self.tabousize, self.maxiter)
        ## Duration in seconds
        self.duration = time.time() - start_time
        self.solution_fitness = self.fitness.calcul(self.solution)
    
    def resolve(self, x: list, tabousize: int, maxiter = 1000):
        xmin = nextx = x
        fx = fmin = fnextx = self.fitness.calcul(x)
        tabou = []
        tabou.append(x)
        C = []

        for i in range(0, maxiter):
            try:
                C = self.voisinage.get_voisins(x , tabou, self.regen_permutations)
            except:
                print("here")
            miny = self.getMinY(C)
            nextx = miny['x']
            fnextx = miny['f']
            
            self.fitness.setValeurActuelle(fnextx)  # Affectation de la valeur actuelle

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
            fy = self.fitness.calcul(y[0],y[1][0],y[1][1])
            if fy < fminy or len(miny) == 0:
                miny = y[0]
                fminy = fy

        return {
            'x' : miny,
            'f' : fminy
        }