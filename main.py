from Models.TaillardParser import TaillardParser

parser = TaillardParser('tai17a.dat')

connexion_matrix = parser.get_distance_matrix()

for i in connexion_matrix:
    print(i)
