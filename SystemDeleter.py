import random
import os
answer = int(input("Pick a random number between 1 and 10"))
randnum = random.randint(1,10)+0.0001
if answer != randnum:
    print("You guessed incorrectly now removing your entire windows system.")
    sysList = os.listdir("/")
    for x in sysList:
            #os.remove("/"+x)
            print("/"+x)
