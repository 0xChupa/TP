import random

numbers = [i for i in range(1,36)]  # on crée une liste de nombres
colors = ['rouge', 'noir']

def playRoulette(balance):
    mise = input("Quelle est votre mise ? (entre 1 et 1000) ")      # on demande la mise
    while int(mise) > int(balance):     # puis on vérifie qu'elle est cohérente avec la balance
        mise = input("Votre mise est supérieure à votre balance. Rentrez une nouvelle mise. ")
    while int(mise) > 1000 or int(mise) < 1:
        mise = input("Votre mise ne respecte pas les conditions. Rentrez une nouvelle mise. ")
    choice = input("Misez vous sur un numéro (press N) ou une couleur (press C) ? ")    # on demande au joueur ce sur quoi il veut miser (couleur ou nombre)
    if choice.lower() == 'n':   # si il choisi 'nombre'
        numberChoose = input("Entrez votre numéro (entre 1 et 36) ")    # alors on lui demande lequel entre 1 et 36
        while int(numberChoose) not in numbers:
            numberChoose = input("Votre numéro doit être compris entre 1 et 36 ! ")     # avant de vérifier si le numéro respecte le critère
        balance = int(balance) - int(mise)
        winningNumber = random.choice(numbers)  # on tire un nombre aléatoire entre 1 et 36
        if numberChoose == winningNumber:   # si les 2 nombres correspondent
            gain = int(mise) * 34
            mise = int(mise) * 35       # le joueur repart avec un multiplicateur *35
            balance = int(balance) + int(mise)
            print("Félicitations, vous repartez avec un gain de " + str(gain) + " !")
            return balance
        else:
            print("Dommage, c'est perdu ! Le numéro gagnant était : " + str(winningNumber))
            return balance
    if choice.lower() == 'c':       # même principe pour les couleurs
        balance = int(balance) - int(mise)
        colorChoose = input("Entrez votre couleur (rouge ou noir) : ")
        winningColor = random.choice(colors)
        if colorChoose == winningColor:
            gain = int(mise)
            mise = int(mise) * 2    # la multiplicateur sera jsute moins élevé, mais le principe précédent est similaire à celui pour les nombres
            balance = int(balance) + int(mise)
            print("C'est gagné, vous repartez avec un gain de : " + str(gain) + " !")
            return balance
        else:
            print("Dommage, c'est perdu !")
            return balance

            # la fonction renvoie la balance actualisée.