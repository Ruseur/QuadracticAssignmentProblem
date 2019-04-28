import unittest
from Models.TaillardParser import TaillardParser

# https://docs.python.org/3/library/unittest.html
class TestAllClasses(unittest.TestCase):

    def setUp(self):
        self.parser = TaillardParser('data_exo3.dat')

    def test_fitness(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
    def test_voisinage(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_recuit(self):
        self.assertTrue('FOO'.isupper())

    def test_tabou(self):
        self.assertTrue('FOO'.isupper())


if __name__ == '__main__':
    unittest.main()