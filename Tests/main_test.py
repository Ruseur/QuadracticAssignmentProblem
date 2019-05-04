import unittest
from Models.TaillardParser import TaillardParser

# https://docs.python.org/3/library/unittest.html
class TestAllClasses(unittest.TestCase):

    def setUp(self):
        self.parser = TaillardParser('data_exo3.dat')

    def test_fitness(self):
        # in : X0   = 13452
        # out: f    = 78
        self.assertEqual(False, 78)

        # in : X    = 43215
        # out: f    = 43
        self.assertEqual(False, 43)
    
    def test_voisinage(self):
        # in : X0   = 13452
        # out: V    = {43152, 12453, 13542, 13425}
        self.assertEqual(False, {43152, 12453, 13542, 13425})

    def test_recuit(self):
        # in : t0   = -12/ln(0.5)
        # out: r    = {43215}
        self.assertEqual(False, {43215})

    def test_tabou(self):
        self.assertEqual(False, True)


if __name__ == '__main__':
    unittest.main()