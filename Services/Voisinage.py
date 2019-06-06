import random

class Voisinage:

    __all_permutations = []

    def __init__(self, distances: list, type="default", *args):
        self.distances = distances
        self.__all_permutations = self.get_permutations(distances)
        if type == "distances":
            self.permutations = self.get_permutations_by_distances(distances, args[0])
        elif type == "random":
            self.permutations = self.get_permutations_random(distances, args[0])
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
        maxint = len(distances)-1

        indexes = list(range(0,maxint))
        random.shuffle(indexes)

        random_indexes = []
        if(taille >= maxint):
            random_indexes = indexes
        else:
            random_indexes = indexes[:taille]

        for index in random_indexes:
            permutations.append(self.__all_permutations[index])

        return permutations

    def get_voisins(self, x: list, exclude = []):
        voisins = []
        voisin = []

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