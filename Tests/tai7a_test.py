import unittest
from Models.TaillardParser import TaillardParser
from Services.Fitness import Fitness
from Services.Voisinage import Voisinage
from Services.Recuit import Recuit
from Services.Tabou import Tabou

# https://docs.python.org/3/library/unittest.html
class TestTai12a(unittest.TestCase):

    def setUp(self):
        self.parser = TaillardParser('tai12a.dat')

    def test_fitness(self):
        
        connexion_matrix = self.parser.get_connexion_matrix()
        distance_matrix = self.parser.get_distance_matrix()

        fitness = Fitness(connexion_matrix, distance_matrix)

        self.assertEqual(fitness.calcul([4, 11, 6, 3, 1, 9, 2, 8, 7, 5, 0, 10]), 224416)
        
    def test_recuit(self):
        distances = self.parser.get_distance_matrix()
        connexions = self.parser.get_connexion_matrix()
        voisinage = Voisinage(distances)
        fitness = Fitness(connexions, distances)
        recuit = Recuit(distances, connexions, voisinage, fitness)
        self.assertEqual(recuit.resolve([0,1,2,3,4,5,6,7,8,9,10,11], 100, 100, 100, 0.9), [7,0,5,1,10,9,2,4,8,6,11,3])


    def test_tabou(self):
        distances = self.parser.get_distance_matrix()
        connexions = self.parser.get_connexion_matrix()
        voisinage = Voisinage(distances)
        fitness = Fitness(connexions, distances)
        tabou = Tabou(distances, connexions, voisinage, fitness)
        self.assertEqual(tabou.resolve(voisinage.get_random_x(), 1000), [7,0,5,1,10,9,2,4,8,6,11,3])


if __name__ == '__main__':
    unittest.main()