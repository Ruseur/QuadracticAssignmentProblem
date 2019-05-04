class Voisinage:

    def __init__(self, distances: list, poids: list, distancesmax: int):
        self.distances = distances
        self.poids = poids
        self.length = len(distances)
        self.distancemax = distancesmax
    
    def getVoisins(self, x: list, exclude = []):
        
        return x