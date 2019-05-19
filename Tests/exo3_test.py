import unittest
from Models.TaillardParser import TaillardParser
from Services.Fitness import Fitness
from Services.Voisinage import Voisinage
from Services.Recuit import Recuit
from Services.Tabou import Tabou

# https://docs.python.org/3/library/unittest.html
class TestExo3(unittest.TestCase):

    def setUp(self):
        self.parser = TaillardParser('data_exo3.dat')

    def test_fitness(self):
        
        connexion_matrix = self.parser.get_connexion_matrix()
        distance_matrix = self.parser.get_distance_matrix()

        fitness = Fitness(connexion_matrix, distance_matrix)
        # in : X0   = 13452
        # out: f    = 78
        self.assertEqual(fitness.calcul([0,2,3,4,1]), 78)

        # in : X    = 43215
        # out: f    = 43
        self.assertEqual(fitness.calcul([3,2,1,0,4]), 43)
    
    def test_voisinage(self):
        distances = self.parser.get_distance_matrix()
        voisinage = Voisinage(distances, "distances", 1)
        # in : X0   = 13452
        # out: V    = {43152, 12453, 13542, 13425}
        self.assertEqual(voisinage.get_voisins([0,2,3,4,1]), [[3,2,0,4,1], [0,2,4,3,1], [0,1,3,4,2], [0,2,3,1,4]])

    def test_recuit(self):
        distances = self.parser.get_distance_matrix()
        connexions = self.parser.get_connexion_matrix()
        voisinage = Voisinage(distances)
        fitness = Fitness(connexions, distances)
        recuit = Recuit(distances, connexions, voisinage, fitness)
        # in : t0   = -12/ln(0.5)
        # out: r    = {43215}
        self.assertEqual(recuit.resolve([0,1,2,3,4], 100, 100, 100, 0.9), [3,2,1,0,4])

    def test_tabou(self):
        distances = self.parser.get_distance_matrix()
        connexions = self.parser.get_connexion_matrix()
        voisinage = Voisinage(distances)
        fitness = Fitness(connexions, distances)
        tabou = Tabou(distances, connexions, voisinage, fitness)
        self.assertEqual(tabou.resolve(voisinage.get_random_x(), 10), [3,2,1,0,4])


if __name__ == '__main__':
    unittest.main()