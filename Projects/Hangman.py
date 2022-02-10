#Biografia de San Ignacio de Loyola

from multiprocessing.connection import wait
import random
import urllib.request
import json
from RandomHipsterStuff import RandomHipsterStuff
import time

hipUrl = "https://random-data-api.com/api/hipster/random_hipster_stuff"


req = urllib.request.Request(hipUrl)
requestData = json.loads(urllib.request.urlopen(req).read())

myHipster = RandomHipsterStuff(**requestData)


hipAr = myHipster.words


def StartGame(hipAr):
    welcome = input("Welcome to my super hipster hangman game?Wanna play?")
    if(welcome == "yes"):
        print("lets get started!!")
        time.sleep(1)
        hipWord = hipAr[0]
        lengthOfWord = len(hipWord)
        
  
        answeLine = ""
        for x in range(lengthOfWord):
           
           answeLine = answeLine + "___   "

       
        for x in range(lengthOfWord):

            print(""" 
     _____________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___
   """)
            print(f"Im thinking of a {lengthOfWord} letter word")
            print(answeLine)
            print(hipWord)
            guess = input("What is your guess?")
            hipLetters = list(hipWord)
            
            for letter in hipLetters:
                if(guess == letter ):
                    time.sleep(2)
                    guessed = guess 
                    correct = True
                    break
                else:
                   guessedWrong = guess
                   correct = False
                   break
        if(correct):
            print("You guessed rigth")
    else:
        print("awww")


    

StartGame(hipAr)


