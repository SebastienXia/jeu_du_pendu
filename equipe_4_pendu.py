# Auteurs : Sébastien.X & Léo.V

#Inportation du module random + importation du fichier liste_mots:

import random 

# Definition local des fonction qu'on va utiliser tout au long de notre programme:

def dessinPendu(nb):    # dessin du pendu donnée par le professeur.
    "Cette fonction dessine pas à pas en forme de liste le pendu"
    tab=[
    """
       +-------+
       |
       |
       |
       |
       |
    ==============
    """,
        """
       +-------+
       |       |
       |       O
       |
       |
       |
    ==============
    """
        ,
    """
       +-------+
       |       |
       |       O
       |       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      | |
       |
    ==============
    """
    ]
    return tab[nb]

def jeu_du_pendu():                                                                                                                             # fonction du jeu du pendu.
    "Cette fonction permet de jouer au pendu lorsqu'on l'appelle"
    print("Bienvenue dans le jeu du pendu !")

    words = [word.strip() for word in open("mots.txt", encoding="utf-8")]                                                                       # ouverture du fichier liste_mots.txt et lecture de chaque mot. 
    mot_a_trouve = random.choice(words)                                                                                                         # random.choice permet de choisir n'importe quel mot dans la liste donnée.
    
    list_du_mot = []
    nliste = []
    for lettres in mot_a_trouve:
        list_du_mot.append(lettres)
        nliste.append("-")

    liste_de_mots_deja_propose = []
    nb_erreur = 0

    while nb_erreur != 6:                                                                                                                        # boucle pour jouer au pendu.

        if mot_a_trouve == "".join(nliste):
            print(f"Bravo ! Vous avez trouvé le mot '{mot_a_trouve}'.")
            break

        lettre_proposer = input("Proposez une lettre : ")
        lettre_proposer = lettre_proposer.upper()                                                                                                # Car la liste de mots est en majuscule (liste donné par le professeur).
   
        if lettre_proposer in list_du_mot:

            for (index,lettres) in enumerate(list_du_mot):
                if lettres == lettre_proposer:
                    nliste[index] = lettres
                mot_cache = "".join(nliste)

            if lettre_proposer not in liste_de_mots_deja_propose:

                print(f"Cette lettre est correcte\n{dessinPendu(nb_erreur)}\n {mot_cache}")
            else:
                print(f"Cette lettre est correcte\nFaite attention, vous avez déjà proposé cette lettre !\n{dessinPendu(nb_erreur)}\n {mot_cache}")

        elif lettre_proposer not in list_du_mot:
            mot_cache = ''.join(nliste)
            nb_erreur += 1
            if lettre_proposer not in liste_de_mots_deja_propose:
                print(f"Cette lettre est incorrecte\n {dessinPendu(nb_erreur)}\n {mot_cache}")
            else:
                print(f"Cette lettre est incorrecte\nEn plus, vous avez déjà proposé cette lettre !\n{dessinPendu(nb_erreur)}\n {mot_cache}")

        liste_de_mots_deja_propose.append(lettre_proposer)

        if nb_erreur == 6:                                                                                                                          # si le nombre d'erreur est égale à 6, on sort de la boucle.
            print(f"Désoler c'est perdu, le mot était '{mot_a_trouve}'")