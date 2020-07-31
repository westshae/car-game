import random
import os
import time

score = [0,0,0,0,0,0]

def start():
    start.username = str(input("Please enter your name: "))

    start.usercar = int(input("Please pick a racecar between 1-6: "))
    if(start.usercar > 6 or start.usercar < 1):
        print("Please pick a number between 1 and 6")
        os._exit(1)

    start.distance = int(input(
        "How far would you like the race to be? Please pick a number between 5-15: "))
    if(start.distance > 5 and start.distance < 5):
        print("")
        os._exit(1)

    print("Great username, ", start.username, ". You have chosen the car number ", start.usercar, " and a distance of ", start.distance, " kilometers.")
    wait = input("Please press enter to continue")

def checkWin():
    checkWin.hasWon = False

    for i in range(6):
        ii = score[i]
        if(ii == start.distance):
            if(i == start.usercar):
                print("Your car won! Congradulations")
                checkWin.hasWon = True
            else:
                print("Unfortunately another car, ", i, ", has won. Better luck next time")
                checkWin.hasWon = True


def round():
    diceroll = random.randint(1, 6)
    score[diceroll - 1] = score[diceroll - 1] + 1
    time.sleep(1)
    os.system('cls')
    
    for i in range(6):
        ii = score[i]
        message = ("car" + str(i + 1) + ": " + ('#' * ii))
        print(message)
    
    checkWin()
        

start()
checkWin()
while checkWin.hasWon == False:
    round()
