import random
from threading import Thread

class Voisinage(Thread):
    __all_permutations = []

    def __init__(self, distances: list, type="default", *args):
        Thread.__init__(self)
        self.distances = distances
        self.__all_permutations = self.get_permutations(distances)
        self.permutations_type = type
        self.permutations_taille = args[0] if args else 0
        self.gen_permutations()

    def run(self):
        """ Code executer au lancement du Thread """
    
    def gen_permutations(self):
        if self.permutations_type == "distances":
            self.permutations = self.get_permutations_by_distances(self.distances, self.permutations_taille)
        elif self.permutations_type == "random":
            self.permutations = self.get_permutations_random(self.distances, self.permutations_taille)
        else:
            self.permutations = self.__all_permutations
    
    def get_permutations_by_distances(self, distances: list, distancesmax = 1):
        '''
           Calcul du voisinage selon la  matrice de distance
        '''
        permutations = []
        i = j = 0

        for y in distances:
            for x in y:
                if (i == j):
                    break
                elif x <= distancesmax and x != 0:
                    permutations.append([i,j])
                i += 1
            i = 0
            j += 1
        
        return permutations

    def get_permutations(self, distances: list):
        '''
           Calcul du voisinage par défaut
        '''
        permutations = []
        length = len(distances)

        for x in range(length):
            for y in range(x+1,length):
                permutations.append([x,y])
        
        return permutations

    def get_permutations_random(self, distances: list, taille: int):
        '''
           Calcul du voisinage par défaut
        '''
        permutations = []
        maxint = len(self.__all_permutations)

        indexes = list(range(0,maxint))
        random.shuffle(indexes)

        i = 0
        while i != maxint and i < taille:
            permutations.append(self.__all_permutations[indexes[i]])
            i = i + 1
        
        return permutations

    def get_voisins(self, x: list, exclude = [], regen_permutations = False):
        voisins = []
        voisin = []
        if regen_permutations:
            self.gen_permutations()

        for permutation in self.permutations:
            a = permutation[0]
            b = permutation[1]

            voisin = x[:a]
            voisin = voisin + [ x[b] ]
            if (b == a + 2):
                voisin = voisin + [ x[a+1] ]
            elif (len(x) == b+1):
                voisin = voisin + x[a+1:b]
            else:
                voisin = voisin + x[a+1:b]
            voisin = voisin + [ x[a] ]
            voisin = voisin + x[b+1:]

            if (voisin not in exclude):
                voisins.append(voisin)

        return voisins

    def get_random_x(self):
        length = len(self.distances)
        x = list(range(0,length))
        x = random.sample(x, length)
        return x
