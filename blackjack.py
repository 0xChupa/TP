import random 

cartes = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]   # on définit les valeurs des différentes cartes (les habillés valent 10, et l'AS vaut 11)

def tirage(cartes):     # on crée une fonction de tirage aléatoire des cartes
    tirage = random.choice(cartes)
    return tirage

def check(x):   # fonction qui permettra de checker la balance du croupier
    if x == 21:
        return 0
    elif x > 21 :
        return 1
    elif 15 < x < 18 :
        return 2
    else:
        return 3

playAgain = 1
double = 0


def playBlackjack(balance):
    double = 0
    mise = input("Quelle est votre mise ? ")
    if int(mise) > int(balance):    # on vérifie que la mise n'excède pas la balance
        mise = input("Votre mise est supérieure à votre balance. Rentrez une nouvelle mise : ")

    balance = int(balance) - int(mise)

    totalJ = 0 + tirage(cartes)     # on fait le premier tour où le joueur reçoit 2 cartes et le croupier une seule.
    totalJ += tirage(cartes)
    totalC = 0 + tirage(cartes)

    if totalJ == 21:    # si le joueur a 21, alors c'est le blackjack, et on mets à jour sa balance
        print("Blackjack !")
        mise = int(mise) * 1.5
        balance = int(balance) + int(mise)
        return balance

    elif totalJ > 21:   # si son score est supérieur à 21, alors il perd.
        print("Le croupier gagne, car votre score est : " + str(totalJ))
        return balance

    else:   # sinon, on rentre dans la boucle de jeu jusqu'à la victoire/défaire du joueur
        print("Vous êtes à un total de : " + str(totalJ) + ", et le croupier a un total de " + str(totalC) + " avec sa première carte.")    # on expose la situation de la partie
        continueToPlayJ = input("Continue ? (Y / N) : ")    # On demande si le joueur veut continuer

        while continueToPlayJ == 'Y':   # si oui, rentre dans la boucle de jeu
            if double == 0:
                answerDouble = input("Voulez-vous doubler votre mise ? (Y/N) ")     # on demande si le joueur souhaite doubler sa mise
            if answerDouble.lower() == 'y':
                double = 1
                if int(mise) <= int(balance):   # on vérifie si sa balance le lui permets si il souhaite doubler 
                    balance = int(balance) - int(mise)
                    mise = int(mise) * 2
                else:
                    print("Votre balance actuelle ne vous permet pas de doubler votre mise.")

            cartePioche = tirage(cartes)    # on pioche une carte
            if int(cartePioche) == 11:
                As = input("Vous avez piocher un as, voulez-vous que celui-ci soit égal à 1 ou à 11 ?")     # si celle-ci est un as, alors le joueur doit choisir si il veut ajouter 1 ou 11 à son score
                if As == '1':
                    totalJ += 1
                else:
                    totalJ += cartePioche
            else:
                totalJ += cartePioche

            if totalJ > 21:     # on check l'état des score du joueur, seulement si il excède 21 ou a un blackjack pour l'instant.
                print("Le croupier gagne, car votre score est : " + str(totalJ))
                return balance
            elif totalJ == 21:
                    print("Blackjack !")
                    mise = int(mise) * 1.5
                    balance = int(balance) + int(mise)
                    return balance
            else:
                print("Vous êtes à un total de : " + str(totalJ))

                continueToPlayJ = input("Continue ? (Y / N) : ")    # on demande au joueur si il veut rejouer. Si c'est le cas, alors on le renvoie au début de la boucle de jeu.

    totalC += tirage(cartes)    # sinon on passe au tirage des cartes du croupier
    if totalJ > 21:
        return balance
    if check(totalC) == 0:  # cas où le croupier a un blackjack
        print("Tu as perdu, le croupier a un Blackjack.")
        return balance

    if check(totalC) == 1:  # cas où le croupier a un score dépassant 21
        if totalJ > 21:
            return balance
        else:
            print("Tu as gagné")
            mise = int(mise) * 1.5
            balance = int(balance) + int(mise)
        return balance


    if check(totalC) == 2:      # cas où le croupier a un score entre 15 et 18
        playC = random.randint(0, 1)    # on tire aléatoirement 0 ou 1 qui déterminera si le croupier repioche ou non.
        if playC == 1:
            totalC += tirage(cartes)
            if check(totalC) == 1:      # puis on recheck tous les cas possibles pour le score du croupier
                mise = int(mise) * 1.5
                balance = int(balance) + int(mise)
                print("Vous avez gagné.")
            if check(totalC) == 0:
                print("Le croupier a un blackjack.")
            if 21 >= totalC > totalJ:
                print("Le croupier gagne avec un score de : " + str(totalC))
            if 21 >= totalJ > totalC:
                print("Vous avez gagné avec un score de : " +  str(totalJ) + " contre " + str(totalC) + "pour le croupier.") 
                mise = int(mise) * 1.5
                balance = int(balance) + int(mise)           
        return balance

    if check(totalC) == 3:      # cas où le croupier a un autre score que les cas précédents, on compare son score à celui du joueur.
        if totalC > totalJ:
            print("Vous avez perdu. Le croupier a " + str(totalC))
            return balance
        elif totalC == totalJ:
            print("Egalite.")
            balance = int(balance) + int(mise)
            return balance
        else:
            if totalJ > 21:
                return balance
            else:
                print("Bien joué, vous avez gagné. Le croupier avait " + str(totalC) + " .")
                mise = int(mise) * 1.5
                balance = int(balance) + int(mise)
                return balance
# le programme renverra la balance actualisée après chaque partie.