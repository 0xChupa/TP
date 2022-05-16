import numpy
import pygame
import time
import sys
import random
from random import choices
solde = 100
PlayAgain = 1
while PlayAgain == 1:
    if  input(" Tappez oui si vous souhaitez jouer ") != "oui":
        print("Merci d'avoir joué, à une prochaine fois !")
        break
    else :
        print("Votre solde s'élève actuellement à", solde , "jetons")
        time.sleep(2)
        if solde <= 0:
            print ("solde insufisant, nous vous créditons de 100 jetons.")
        rep1=str(input("Voulez-vous miser sur un numéro ou une couleur (mettez bien votre réponse avec la même orthographe)? \n"))
    if rep1=="numéro" or rep1=="un numéro" or rep1=="couleur" or rep1=="une couleur":
        if rep1=="numéro" or rep1=="un numéro":
            rep=int(input("Faites vos jeux! Miser sur un numéro (entre 1 et 36).\n"))
            if rep <1 or rep > 36 or rep == True:
                print("Nous vous avons dit un nombre entre 1 et 36 et pas", rep, ". Veuillez relancer le programme!")
                exit()
            mise=int(input("Combien misez-vous (entre 1 et 1000 jetons)? \n "))
            while True:
                if (mise > 1000 or mise < 1):
                    print("Nous vous avons dit entre 1 et 1000 jetons et pas", mise, "\n")
                    mise = int(input("Choisissez cette fois ci une mise entre 1 et 1000 jetons"))
                break
            else:
                break

            solde1 = solde - mise
            print("Votre solde s'élève alors à", solde1, "jetons")

            print("Si la bille tombe sur le numéro sur lequel vous avez misé, alors vous repartirez avec votre mise + votre mise x35. Bonne chance! \n")
            nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
            cousor=choices(nums)
            if cousor[0]==rep:
                gain = 35*mise
                time.sleep(2)
                print("Votre mise était de", mise, "jetons;")
                time.sleep(1)
                print("Vous avez misé sur le numéro", rep, ";")
                time.sleep(1)
                print("Et la bille est tombée sur numéro...")
                time.sleep(3)
                print(cousor, "\n")
                time.sleep(1)
                print("Vous avez donc gagné, vous repartez avec", gain, "jetons. félicitation !")
                A = 0
            else:
                print("Votre mise était de", mise, "jetons;")
                time.sleep(1)
                print("Vous avez misé sur le numéro", rep, ";")
                time.sleep(1)
                print("Et la bille est tombée sur le numéro...")
                time.sleep(3)
                print(cousor, "\n")
                time.sleep(1)
                print("Vous avez donc perdu, vous perdez donc", mise, "jetons")
                gain = -mise
                A = 1                                                                   #permet de rentrer dans la boucle de perte à la fin du programme.
        if rep1=="couleur" or rep1=="une couleur":
            rep=str(input("Faites vos jeux! Miser sur une couleur (rouge ou noir).\n "))
            if rep=="rouge" or rep=="noir" or rep=="le noir" or rep=="le rouge":
                mise=int(input("misez-vous (entre 1 et 1000 jetons)?\n"))
                while True:
                       if (mise>1000 or mise<1):
                           print("Nous vous avons dit entre 1 et 1000 jetons et pas", mise , "\n")
                           mise = int(input("Choisissez cette fois ci une mise entre 1 et 1000 jetons"))
                       break

                else :
                    break

                solde1 = solde - mise
                print ("Votre solde s'élève alors à" , solde1 , "jetons")

                print("Si la bille tombe sur la couleur sur laquelle vous avez misé, alors vous repartirez avec votre mise x2. Bonne chance! \n")

                val=random.random()
                if val >= 0.5 :
                    cousor0 = "noir"
                else :
                    cousor0 = "rouge"
                if cousor0==rep:
                    gain = 2*mise
                    print("Votre mise était de", mise, "jetons;")
                    time.sleep(1)
                    print("Vous avez misé sur la couleur", rep, ";")
                    time.sleep(1)
                    print("Et la bille est tombée sur la couleur...")
                    time.sleep(3)
                    print(cousor0, "\n")
                    time.sleep(1)
                    print("Vous avez donc gagné, vous obtenez", gain, "jetons. félicitation !")
                    A = 0
                else:
                    print("Votre mise était de", mise, "jetons;")
                    time.sleep(1)
                    print("Vous avez misé sur la couleur", rep, ";")
                    time.sleep(1)
                    print("Et la bille est tombée sur la couleur...")
                    time.sleep(3)
                    print(cousor0, "\n")
                    time.sleep(1)
                    print("Vous avez donc perdu, vous perdez donc", mise, "jetons")
                    gain = -mise
                    A = 1                                                                       #permet de rentrer dans la boucle de perte à la fin du programme
            else:
                print("Vous avez répondu", rep, "et cette réponse n'est pas appropriée! Veuillez relancer le programme!")
    else:
        print("Vous avez répondu", rep1, "et cette réponse n'est pas appropriée! Veuillez relancer le programme!")

    if A == 1:
        solde = solde1
        print ("votre solde s'élève à" , solde , "jetons")
    else:
        solde = solde1 + gain
        print("Votre solde s'élève à" , solde , "jetons.")

    if solde < 0:
        print( " vous n'avez plus de jeton. réésayez une autre fois !")
        exit()
if input("Voulez vous rejouer ?") != "oui":
    PlayAgain = 0