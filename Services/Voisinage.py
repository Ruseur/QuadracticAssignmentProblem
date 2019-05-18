class Voisinage:

    def __init__(self, distances: list, distancesmax=1):
        self.distances = distances
        self.distancemax = distancesmax
        self.permutations = self.get_permutations(distances)
    
    def get_permutations(self, distances: list):
        permutations = []
        i = j = 0

        for y in distances:
            for x in y:
                if (i == j):
                    break
                elif x <= self.distancemax and x != 0:
                    permutations.append([i,j])
                i += 1
            i = 0
            j += 1
        
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