import random

numbers = [i for i in range(1,36)]
colors = ['rouge', 'noir']

def playRoulette(balance):
    mise = input("Quelle est votre mise ? (entre 1 et 1000) ")
    while int(mise) > int(balance):
        mise = input("Votre mise est supérieure à votre balance. Rentrez une nouvelle mise. ")
    while int(mise) > 1000 or int(mise) < 1:
        mise = input("Votre mise ne respecte pas les conditions. Rentrez une nouvelle mise. ")
    choice = input("Misez vous sur un numéro (press N) ou une couleur (press C) ? ")
    if choice.lower() == 'n':
        numberChoose = input("Entrez votre numéro (entre 1 et 36) ")
        while int(numberChoose) not in numbers:
            numberChoose = input("Votre numéro doit être compris entre 1 et 36 ! ")
        balance = int(balance) - int(mise)
        winningNumber = random.choice(numbers)
        if numberChoose == winningNumber:
            gain = int(mise) * 34
            mise = int(mise) * 35
            balance = int(balance) + int(mise)
            print("Félicitations, vous repartez avec un gain de " + str(gain) + " !")
            return balance
        else:
            print("Dommage, c'est perdu !")
            return balance
    if choice.lower() == 'c':
        balance = int(balance) - int(mise)
        colorChoose = input("Entrez votre couleur (rouge ou noir) : ")
        winningColor = random.choice(colors)
        if colorChoose == winningColor:
            gain = int(mise)
            mise = int(mise) * 2
            balance = int(balance) + int(mise)
            print("C'est gagné, vous repartez avec un gain de : " + str(gain) + " !")
            return balance
        else:
            print("Dommage, c'est perdu !")
            return balance