import random 

cartes = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

def tirage(cartes):
    tirage = random.choice(cartes)
    return tirage

def check(x):
    if x == 21:
        print("Tu as perdu, le croupier a un Blackjack.")
        return 0
    elif x > 21 :
        print("Tu as gagné")
        return 1
    elif 15 < x < 18 :
        return 2
    else:
        return 3

playAgain = 1
balance = input("Avec combien commencez-vous à jouer ? ")

while playAgain != 'N':
    print("Votre balance est désormais : ", balance)
    mise = input("Quelle est votre mise ? ")
    if int(mise) > int(balance):
        mise = input("Votre mise est supérieure à votre balance. Rentrez une nouvelle mise : ")

    balance = int(balance) - int(mise)

    totalJ = 0 + tirage(cartes)
    totalJ += tirage(cartes)
    totalC= 0 + tirage(cartes)

    if totalJ == 21:
        print("Blackjack !")
        mise = int(mise) * 1.5
        balance = int(balance) + int(mise)

    else:
        print("Vous êtes à un total de : " + str(totalJ) + ", et le croupier a un total de " + str(totalC) + " avec sa première carte.")
        continueToPlayJ = input("Continue ? (Y / N) : ")

        while continueToPlayJ == 'Y':
            cartePioche = tirage(cartes)
            if cartePioche == '11' and totalJ + cartePioche > 21:
                totalJ +=1
            else:
                totalJ += tirage(cartes)
            if totalJ > 21:
                print("Le croupier gagne")
                break
            elif totalJ == 21:
                print("Blackjack !")
                mise = int(mise) * 1.5
                balance = int(balance) + int(mise)
                break
            else:
                print("Vous êtes à un total de : " + str(totalJ))
            
            continueToPlayJ = input("Continue ? (Y / N) : ")

        totalC += tirage(cartes)
        if check(totalC) == 0:
            break

        if check(totalC) == 1:
            if totalJ > 21:
                break
            else:
                mise = int(mise) * 1.5
                balance = int(balance) + int(mise)

        if check(totalC) == 2:
            playC = random.randint(0,1)
            if playC == 1:
                totalC += tirage(cartes)
                if check(totalC) == 1:
                    mise = int(mise) * 1.5
                    balance = int(balance) + int(mise)
        
        if check(totalC) == 3:
            if totalC > totalJ:
                print("Vous avez perdu. Le croupier a " + str(totalC))
            elif totalC == totalJ:
                print("Egalite.")
                balance =  int(balance) + int(mise)
            else:
                if totalJ > 21:
                    continue
                else:
                    print("Bien joué, vous avez gagné.") 
                    mise = int(mise) * 1.5
                    balance = int(balance) + int(mise)

    playAgain = input("Play Again ( Yes (press Y) or No (press N) ) : ")
