import unittest
import math
from Models.TaillardParser import TaillardParser
from Services.Voisinage import Voisinage
from Services.Recuit import Recuit
from Services.Tabou import Tabou

# https://docs.python.org/3/library/unittest.html
class TestAllClasses(unittest.TestCase):

    def setUp(self):
        self.parser = TaillardParser('data_exo3.dat')
        self.distances = self.parser.get_distance_matrix()
        self.connexions = self.parser.get_connexion_matrix()

    def test_fitness(self):
        # in : X0   = 13452
        # out: f    = 78
        self.assertEqual(False, 78)

        # in : X    = 43215
        # out: f    = 43
        self.assertEqual(False, 43)
    
    def test_voisinage(self):
        voisinage = Voisinage(self.distances)
        # in : X0   = 13452
        # out: V    = {43152, 12453, 13542, 13425}
        self.assertEqual(voisinage.get_voisins([0,2,3,4,1]), [[3,2,0,4,1], [0,2,4,3,1], [0,1,3,4,2], [0,2,3,1,4]])

    def test_recuit(self):
        voisinage = Voisinage(self.distances)
        recuit = Recuit(self.distances, self.connexions, voisinage)
        # in : X0   = [1,3,4,5,2]
        # in : t0   = -12/ln(0.5)
        # out: r    = [4,3,2,1,5]
        self.assertEqual(recuit.resolve([0,2,3,4,1], -12/math.log(0.5), 5, 5, 0.01), [3,2,1,0,4])

    def test_tabou(self):
        self.assertEqual(False, True)


if __name__ == '__main__':
    unittest.main()