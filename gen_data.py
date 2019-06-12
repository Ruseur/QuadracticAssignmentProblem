from Models.TaillardParser import TaillardParser
from Services.Fitness import Fitness
from Services.Voisinage import Voisinage
from Services.Recuit import Recuit
from Services.Tabou import Tabou
from threading import Thread

import time
import datetime
import multiprocessing as mp



def gen_data(input_data = [], nb_par_data = 200):
    start_time = time.time()
    print(datetime.datetime.fromtimestamp(start_time))
    list_i = range(0, nb_par_data)
    list_recuit = []
    # Je démarre tous les threads necessaires
    for input in input_data :
        print(input)
        print(datetime.datetime.fromtimestamp(time.time()))
        parser = TaillardParser(input)
        voisinage = Voisinage(parser.get_distance_matrix(), "random", 50)
        fitness = Fitness(parser.get_connexion_matrix(), parser.get_distance_matrix())
        recuit = Recuit(parser.get_distance_matrix(), parser.get_connexion_matrix(), voisinage, fitness, True)
        for i in list_i:
            recuit = Recuit(parser.get_distance_matrix(), parser.get_connexion_matrix(), voisinage, fitness)
            recuit.init_values(voisinage.get_random_x(), 100, 100, 100, 0.9)
            print(input + " - " + str(i))
            list_recuit.append(recuit)
    
    print("Fin instanciation recuits")
    print("Temps necessaire: {}".format(time.time() - start_time))
    for recuit in list_recuit:
        recuit.start()

    # On attend que tous les threads se terminent
    print("Fin lancement threads")
    step_time = time.time()
    print("Temps necessaire: {}".format(step_time - start_time))

    for recuit in list_recuit:
        recuit.join()
    
    print("Fin d'execution des threads")
    end_time = time.time()
    print("Temps necessaire: {}".format(end_time - start_time))



list_data = ["tai12a.dat", "tai15a.dat", "tai17a.dat", "tai20a.dat", "tai25a.dat", "tai30a.dat"]
gen_data(list_data, 200)



