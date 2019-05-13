from Services.Fitness import Fitness
from Models.TaillardParser import TaillardParser

import random

parser = TaillardParser('data_exo3.dat')
connexion_matrix = parser.get_connexion_matrix()
distance_matrix = parser.get_distance_matrix()

fitness = Fitness(connexion_matrix, distance_matrix)


test = [1, 0, 2, 4, 3]

random.shuffle(test)

print(test)

# print(fitness.calcul())
print(fitness.calcul(test))
# print(fitness.calcul([1, 2], 1, 2))

