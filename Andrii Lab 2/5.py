import random

score_computer = 0
score_player = 0
 # робимо гру до трьох перемог
while score_computer <3 and score_player <3:
    ver = 0
    while (ver == 0):
            print ("-----------------------------------------------------")
            player = int(input("1 - камінь, 2 - ножиці, 3 - папір. "))
            if (player == 1 or player == 2 or player == 3):
                ver = 1
    if player == 1:
            print("Ви обрали камінь.")
    if player == 2:
            print("Ви обрали ножиці.")
    if player == 3:
            print("Ви обрали папір.")
    comp = random.randint(1, 3)
    if comp == 1:
            print("Комп'ютер обрав камінь.")
    if comp == 2:
            print("Комп'ютер обрав ножиці.")
    if comp == 3:
            print("Комп'ютер обрав папір.")
    # визначемо переможця конкретного раунду
    if player == comp:
            win = 0
    if player == 1 and comp == 2:
            win = 1
    if player == 1 and comp == 3:
            win = 2
    if player == 2 and comp == 1:
            win = 2
    if player == 2 and comp == 3:
            win = 1
    if player == 3 and comp == 1:
            win = 1
    if player == 3 and comp == 2:
            win = 2
    if win == 0:
            print("Нічия!")
    if win == 1:
            print("Ви перемогли!")
            score_player +=1
            print("Рахунок:", score_player, "-", score_computer)
    if win == 2:
            print("Ви програли!")
            score_computer +=1
            print("Рахунок:", score_player, "-", score_computer)
# визначемо переможця всієї гри
print ("---------Кінець гри---------")
if score_player == 3:
    print ("Ви виграли із загальним рахунком", score_player, "-", score_computer)
elif score_computer == 3:
    print ("Ви програли із загальним рахунком", score_player, "-", score_computer)
