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

specialChar = ["!","@","#","$","%","^","&","*","(",")","-","+","[","}","{","]","="]
guessedWords= []
correctWords=[]
def getInput() :
    while(True):
     
        guess=input("What is your guess?")
       
        if guess.isnumeric()== True :
            print("Cant be a number")
            continue

        if len(guess)!=1 :
            print("Must only be one letter")
            continue
        if not guess.isalpha():
            print("Can't include special characters")
            continue
        if(guess in guessedWords):
            print("Bruh you already guessed it fracaso")
            continue
        return guess

def Ronda(hipAr):
     hipWord = hipAr[0]
     lengthOfWord = len(hipWord)
        
  
     answeLine = ""
     for x in range(lengthOfWord):
           
           answeLine = answeLine + "___   "
         
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
     guess = getInput()
     
     hipLetters = list(hipWord)
     for letter in hipLetters:
                if(guess == letter ):
                    time.sleep(2)
                    
                    correct = True
                    correctWords.append(guess)
                    
                    break
                else:
                   guessedWrong = guess
                   correct = False

                   break
     guessedWords.append(guess)
     

     if(correct):
            print("You guessed rigth")
     else:
            print("You guessed wrong")




def StartGame(hipAr):
    welcome = input("Welcome to my super hipster hangman game?Wanna play?")
    if(welcome == "yes"):
        print("lets get started!!")
        time.sleep(1)
        Ronda(hipAr)
    
           
    else:
        print("awww")



StartGame(hipAr)


