from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = []
comp = []

def add_user():
    while True:
        b = random.randint(0, 12)
        if b in user:
            b = random.randint(0, 12)
        else:
            user.append(b)
            break

def add_comp():
    while True:
        cb = random.randint(0, 12)
        if cb in user:
            cb = random.randint(0, 12)
        else:
            comp.append(cb)
            break

def show_u():
    print("User cards are as follows:")
    sum_u = 0
    for i in user:
        print(cards[i])
        if cards[i] == 11 and sum_u > 15:
            sum_u += 1
        else:
            sum_u += cards[i]
    print(f"Sum of user cards: {sum_u}")
    return sum_u

def sum_u():
    sum_u = 0
    for i in user:
        if cards[i] == 11 and sum_u > 15:
            sum_u += 1
        else:
            sum_u += cards[i]
    return sum_u

def sum_comp():
    sum_com = 0
    for i in comp:
        sum_com += cards[i]
    if 1 in comp and sum_com >= 20:
        sum_com -= 10
    print(f"Computer sum was: {sum_com}")
    return sum_com

def show_user():
    for i in user:
        print(f"User cards: {cards[i]}")

def show_comp():
    print(f"Computer's first card is: {cards[comp[0]]}")

print(logo)

for i in range(2):
    add_user()

for i in range(2):
    add_comp()

print("Cards distributed are:")
show_comp()
show_user()

hit = input("Enter 'y' if user wants to hit else 'a': ").lower()
while hit == 'y' or hit == 'a':
    if hit == 'y':
        us = show_u()
        cs = sum_comp()
        if us == cs:
            print(f"The game was a draw!!! \nWith score {us}")
        elif us > cs and us <= 21:
            print(f"Computer score was {cs}. Hence, the user wins the game with a score of {us}.")
        elif cs > us and cs > 21:
            print(f"Computer score was {cs}. Hence, the user wins with a score of {us}.")
        elif us > cs and us > 21:
            print(f"Computer score was {cs}. Hence, the user lost with a score of {us}.")
        else:
            print(f"Computer won the game with score {cs}. The user lost with score {us}.")
        hit = input("If user wants more cards, enter 'y'. Else 'n'. Enter 'end' to exit the game:")
         
    elif hit == 'a':
        show_user()
        show_comp()
        hit = input("If user wants more cards, enter 'a'. Else 'y' to HIT. Enter 'end' to exit the game:")
        if hit == 'a':
            add_user()
        sc = sum_comp()
        if sc < 21:
            cn = random.randint(1, 10)
            if cn % 2 == 0: 
                add_comp()
        g = sum_u()
        if g > 21:
            print("User lost the game")
            show_user()
            break

print("HOPE YOU ENJOYED THE GAME! *_*!")