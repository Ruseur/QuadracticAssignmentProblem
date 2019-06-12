class Fitness:
    from random import randint

    def __init__(self, connexion_matrix, distance_matrix):
        self.connexion_matrix = connexion_matrix
        self.distance_matrix = distance_matrix
        self.valeur = 0

    # End point
    def calcul(self, *args):
        """
        Calcul de la fitness d'un voisinage
        :param args:
            args[0] tableau qui indique le placement des elements à relier dans les différents emplacemnts
            args[1] id de l'emplacement 1 sur lequel on a placé l'équipement de l'emplacement 2
            args[2] id de l'emplacement 2 sur lequel on a placé l'équipement de l'emplacement 1
        :return: fitness random|brute|opti
        """

        if args:
            if len(args) > 1:
                return self.calcul_opti(args[0], args[1], args[2])
            else:
                return self.calcul_all(args[0])
        return self.calcul_dummy()

    def calcul_dummy(self):
        return self.randint(1, 100)

    def calcul_all(self, placement_array):
        """
        Calcul de la totalité de la fitness d'un voisinage en fonction des matrices en attributs de classe
        :param placement_array: placement des equipements
        :return:
        """
        # todo prévoir une fonction pour vérifier que les matrices sont de la meme largeur que le nombre d'quipements

        fitness = 0

        for id_emplacement in range(0, len(placement_array)):
            id_equipement = placement_array[id_emplacement]

            # parcourir les equipements qui lui sont relies (connexion matrix)
            for id_equipement_relie in range(0, id_equipement):

                cout_relie = self.connexion_matrix[id_equipement][id_equipement_relie]

                id_emplacement_relie = placement_array.index(id_equipement_relie)

                # print(id_emplacement_relie)
                distance = self.distance_matrix[id_emplacement][id_emplacement_relie]

                fitness += distance * cout_relie

        self.valeur = fitness * 2  # on stocke la valeur de fitness pour optimiser le calcul

        return self.valeur

    def calcul_opti(self, placement_array, id_position_changed_1, id_position_changed_2):
        if self.valeur == 0: # si pas de valeur deja calcule alors on fait le calcul général
            return self.calcul_all(placement_array)
        else:
            delta = 0
            id_equipement_1 = placement_array[id_position_changed_1]
            id_equipement_2 = placement_array[id_position_changed_2]

            for id_emplacement in range(0, len(placement_array)):
                if id_emplacement != id_position_changed_1 and id_emplacement != id_position_changed_2:
                    value_k = placement_array[id_emplacement]
                    delta += (self.connexion_matrix[id_equipement_1][value_k] - self.connexion_matrix[id_equipement_2][value_k]) * (self.distance_matrix[id_position_changed_1][id_emplacement] - self.distance_matrix[id_position_changed_2][id_emplacement])

            self.valeur += delta

            return self.valeur
