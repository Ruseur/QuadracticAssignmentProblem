from Models.TaillardParser import TaillardParser
from Services.Fitness import Fitness
from Services.Voisinage import Voisinage
from Services.Recuit import Recuit
from Services.Tabou import Tabou
from threading import Thread

import time
import datetime
import csv

def gen_data_recuit(input = "", version = 1, nb_par_data = 200):
    start_time = time.time()
    print(datetime.datetime.fromtimestamp(start_time))
    list_i = range(0, nb_par_data)
    list_recuit = []
    # Je démarre tous les threads necessaires
    print(input)
    print(datetime.datetime.fromtimestamp(time.time()))
    parser = TaillardParser(input+'.dat')
    voisinage = Voisinage(parser.get_distance_matrix(), "random", 50)
    fitness = Fitness(parser.get_connexion_matrix(), parser.get_distance_matrix())
    
    for i in list_i:
        recuit = Recuit(parser.get_distance_matrix(), parser.get_connexion_matrix(), voisinage, fitness, True)
        recuit.init_values(voisinage.get_random_x(), 100, 50, 50, 0.3)
        list_recuit.append(recuit)
    
    print("Fin instanciation recuits")
    print("Temps necessaire: {}".format(time.time() - start_time))
    i = 0
    for recuit in list_recuit:
        print(str(i))
        i = i + 1
        recuit.start()

    # On attend que tous les threads se terminent
    print("Fin lancement threads")
    step_time = time.time()
    print("Temps necessaire: {}".format(step_time - start_time))

    for recuit in list_recuit:
        recuit.join()
        print(str(recuit.solution_fitness) + " - " + str(recuit.duration))
    
    print("Fin d'execution des threads")
    end_time = time.time()
    print("Temps necessaire: {}".format(end_time - start_time))

    print("Ecriture CSV")
    with open('data/exports/recuit/v'+ str(version)+ "_" +  input + '.csv', mode='w', newline="\n", encoding="utf-8") as output_file:
        fieldnames = ['initial', 'solution', 'fitness', 'duration']
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        for recuit in list_recuit:
            writer.writerow({
                'initial': "".join(str(e) for e in recuit.x),
                'solution': "".join(str(e) for e in recuit.solution),
                'fitness': recuit.solution_fitness,
                'duration': recuit.duration
            })

def gen_data_tabou(input = "", version = 1, nb_par_data = 50):
    start_time = time.time()
    print(datetime.datetime.fromtimestamp(start_time))
    list_i = range(0, nb_par_data)
    list_tabou = []
    # Je démarre tous les threads necessaires
    print(input)
    print(datetime.datetime.fromtimestamp(time.time()))
    parser = TaillardParser(input+'.dat')
    voisinage = Voisinage(parser.get_distance_matrix(), "random", 50)
    fitness = Fitness(parser.get_connexion_matrix(), parser.get_distance_matrix())
    
    for i in list_i:
        tabou = Tabou(parser.get_distance_matrix(), parser.get_connexion_matrix(), voisinage, fitness, True)
        tabou.init_values(voisinage.get_random_x(), 50, 250)
        list_tabou.append(tabou)
    
    print("Fin instanciation tabou")
    print("Temps necessaire: {}".format(time.time() - start_time))
    i = 0
    for tabou in list_tabou:
        print(str(i))
        i = i + 1
        tabou.start()

    # On attend que tous les threads se terminent
    print("Fin lancement threads")
    step_time = time.time()
    print("Temps necessaire: {}".format(step_time - start_time))

    for recuit in list_tabou:
        recuit.join()
        print(str(recuit.solution_fitness) + " - " + str(recuit.duration))
    
    print("Fin d'execution des threads")
    end_time = time.time()
    print("Temps necessaire: {}".format(end_time - start_time))


    print("Ecriture CSV")
    with open('data/exports/tabou/v'+ str(version)+ "_" +  input + '.csv', mode='w', newline="\n", encoding="utf-8") as output_file:
        fieldnames = ['initial', 'solution', 'fitness', 'duration']
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        for tabou in list_tabou:
            writer.writerow({
                'initial': "".join(str(e) for e in tabou.x),
                'solution': "".join(str(e) for e in tabou.solution),
                'fitness': tabou.solution_fitness,
                'duration': tabou.duration
            })

list_data = ["tai12a", "tai15a", "tai17a", "tai20a", "tai25a", "tai30a", "tai35a", "tai40a", "tai50a", "tai60a", "tai80a", "tai100a"]

for data in list_data:
    gen_data_recuit(data, 3, 50)

for data in list_data:
    gen_data_tabou(data, 3, 50)