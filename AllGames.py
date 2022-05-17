from bingo import playBingo
from blackjack import playBlackjack
from machineSous import playMachineSous

game = input("A quel jeu veux-tu jouer ? ")
balance = input("Quelle est votre balance ? ")
changeGame = 'P'

while changeGame.lower() != 's':
    if game.lower() == 'bingo':
        balance = playBingo(balance)
        print("Votre balance est : " + str(balance))
    if game.lower() == 'blackjack':
        balance = playBlackjack(balance)
        print("Votre balance est : " + str(balance))
    if game.lower() == 'machinesous':
        balance = playMachineSous(balance)
        print("Votre balance est : " + str(balance))
    changeGame = input("Voulez-vous continuer (press P), changer de jeu (press C) ou arrêter (press S).")
    if changeGame.lower() == 'p':
        continue
    if changeGame.lower() == 'c':
        game = input("A quel jeu veux-tu jouer ? ")


print("A bientôt.")