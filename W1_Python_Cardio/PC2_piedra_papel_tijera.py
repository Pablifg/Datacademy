# -*- coding: utf-8 -*-
import random

OPTIONS = ['Piedra', 'Papel', 'Tijera']

def game(winner, loser):
    cont = 0

    if(loser == 0 and winner == 1):
        cont = 1
    if(loser == 1 and winner == 2):
        cont = 1
    if(loser == 2 and winner == 0):
        cont = 1

    return cont

def main():

    attemps = 0
    cont_1 = 0
    cont_2 = 0

    while True:
        attemps += 1

        player2 = random.choice(range(len(OPTIONS)))
        player1 = int(input(""" Escoge:
        1) Piedra
        2) Papel
        3) Tijera\
        """))
        
        print("\nYou choose: ", OPTIONS[player1-1])
        print("Computer chooses: ", OPTIONS[player2], player2 )
        
        print("*" * 50)

        
        cont_1 += game(player1-1, player2)
        cont_2 += game(player2, player1-1)

        if(cont_1 > 2):
            print("=" * 50)
            print("You won the game!! Excellent")
            print(f"You win {cont_1} of {attemps} times")
            break
        elif(cont_2 > 2):
            print("=" * 50)
            print("Oh no! You lost the game :c")
            print(f"Computer won {cont_2} of {attemps} times")
            break



if __name__ == '__main__':
    main()
