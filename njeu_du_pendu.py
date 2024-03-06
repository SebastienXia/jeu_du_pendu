# Auteurs : Sébastien.X & Léo.V

#Inportation du module random + importation du fichier liste_mots:

import random  
from liste_mots import liste_de_mots

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

def jeu_du_pendu():                                                 # fonction du jeu du pendu.
    "Cette fonction permet de jouer au pendu lorsqu'on l'appelle"

    mot_a_trouve = random.choice(liste_de_mots)                     # random.choice permet de choisir n'importe quel mot dans la liste donnée.
    
    list_du_mot = []
    nliste = []
    for lettres in mot_a_trouve:
        list_du_mot.append(lettres)
        nliste.append("-")

    liste_de_mots_deja_propose = []
    nb_points = 0
    nb_erreur = 0
    print(mot_a_trouve)

