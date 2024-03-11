# Teste de chaque fonction du pendu.

from equipe_4_pendu import jeu_du_pendu, dessinPendu

for i in range(7):          # boucle pour afficher les 7 étapes du pendu.
    print(dessinPendu(i))
    print("\n")

jeu_du_pendu()              # appelle de la focntion jeu_du_pendu() pour jouer au pendu.