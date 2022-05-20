from bingo import playBingo
from blackjack import playBlackjack
from machineSous import playMachineSous
from roulette import playRoulette

game = input("A quel jeu veux-tu jouer ? ")
balance = input("Quelle est votre balance ? ")
changeGame = 'P'

while changeGame.lower() != 's':
    if game.lower() == 'bingo':
        balance = playBingo(balance)
        if balance <= 0:
            break
        print("Votre balance est : " + str(balance) + "\n")
    if game.lower() == 'blackjack':
        balance = playBlackjack(balance)
        if balance <= 0:
            break
        print("Votre balance est : " + str(balance) + "\n")
    if game.lower() == 'machinesous':
        balance = playMachineSous(balance)
        if balance <= 0:
            break
        print("Votre balance est : " + str(balance) + "\n")
    if game.lower() == 'roulette':
        balance = playRoulette(balance)
        if balance <= 0:
            break
        print("Votre balance est : " + str(balance) + "\n")
    changeGame = input("Voulez-vous continuer (press P), changer de jeu (press C) ou arrêter (press S).")
    print("\n")
    if changeGame.lower() == 'p':
        continue
    if changeGame.lower() == 'c':
        game = input("A quel jeu veux-tu jouer ? ")

if balance <= 0:
    print("\nVotre balance est nulle. Vous ne pouvez plus jouer.")
print("A bientôt.")