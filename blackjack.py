import random
import pygame

cartes = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

def tirage(cartes):
    tirage = random.choice(cartes)
    return tirage

def check(x):
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
    pygame.init()
    x = 640  # Definition de la taille de la fenêtre
    y = 480

    fenetre2 = pygame.display.set_mode((x, y))

    fond = pygame.image.load("fond.jpg").convert()  # Chargement du fond
    fenetre2.blit(fond, (0, 0))
    double = 0
    mise = input("Quelle est votre mise ? ")
    if int(mise) > int(balance):
        mise = input("Votre mise est supérieure à votre balance. Rentrez une nouvelle mise : ")

    balance = int(balance) - int(mise)

    totalJ = 0 + tirage(cartes)
    totalJ += tirage(cartes)
    totalC = 0 + tirage(cartes)

    if totalJ == 21:
        print("Blackjack !")
        mise = int(mise) * 1.5
        balance = int(balance) + int(mise)
        return balance

    elif totalJ > 21:
        print("Le croupier gagne, car votre score est : " + str(totalJ))
        return balance

    else:
        print("Vous êtes à un total de : " + str(totalJ) + ", et le croupier a un total de " + str(totalC) + " avec sa première carte.")
        continueToPlayJ = input("Continue ? (Y / N) : ")

        while continueToPlayJ == 'Y':
            if double == 0:
                answerDouble = input("Voulez-vous doubler votre mise ? (Y/N) ")
            if answerDouble.lower() == 'y':
                double = 1
                if int(mise) <= int(balance):
                    balance = int(balance) - int(mise)
                    mise = int(mise) * 2
                else:
                    print("Votre balance actuelle ne vous permet pas de doubler votre mise.")

            cartePioche = tirage(cartes)
            if int(cartePioche) == 11:
                As = input("Vous avez piocher un as, voulez-vous que celui-ci soit égal à 1 ou à 11 ?")
                if As == '1':
                    totalJ += 1
                else:
                    totalJ += cartePioche
            else:
                totalJ += cartePioche
            if totalJ > 21:
                print("Le croupier gagne, car votre score est : " + str(totalJ))
                return balance
            elif totalJ == 21:
                    print("Blackjack !")
                    mise = int(mise) * 1.5
                    balance = int(balance) + int(mise)
                    return balance
            else:
                print("Vous êtes à un total de : " + str(totalJ))

                continueToPlayJ = input("Continue ? (Y / N) : ")

    totalC += tirage(cartes)
    if totalJ > 21:
        return balance
    if check(totalC) == 0:
        print("Tu as perdu, le croupier a un Blackjack.")
        return balance

    if check(totalC) == 1:
        if totalJ > 21:
            return balance
        else:
            print("Tu as gagné")
            mise = int(mise) * 1.5
            balance = int(balance) + int(mise)
        return balance


    if check(totalC) == 2:
        playC = random.randint(0, 1)
        if playC == 1:
            totalC += tirage(cartes)
            if check(totalC) == 1:
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

    if check(totalC) == 3:
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
