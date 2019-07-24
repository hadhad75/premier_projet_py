'''nombre à deviner'''
from random import randint
entier = randint(1,1000)

print("""Bienvenue dans LE JUSTE PRIX \n C'est très simple, vous devez trouver 
      le prix d'un article dont le prix est compris entre 1 et 1000€ en 10 essais : \n
      si le nombre proposé est plus grand que le JUSTE PRIX, C'est Moins \n
      si le nombre proposé est plus petit que le JUSTE PRIX, C'est Plus\n""")

for nb_essai in range(1,11):
    print("Il vous reste :",11-nb_essai,"essai(s)")
    ''' proposition de l'utilisateur'''
    entree=int(input("Entrez votre nombre : \n"))
    if nb_essai!=0:
        if entree<entier :
            print("C'est plus !")
        elif entree>entier:
            print("C'est moins !")
        else:
            break

if entier!=entree :
    print("c perdu ! Le juste prix était :", entier,"!")
else :
    print("C'est gagné")

print("Merci d'avoir participé, et à bientôt dans LE JUSTE PRIX")
