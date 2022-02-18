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
count = 0
hipWord = hipAr[0]
correctIndex=[]

specialChar = ["!","@","#","$","%","^","&","*","(",")","-","+","[","}","{","]","="]
guessedWords= []
correctWords=[]
finished = False
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
       # if(guess in guessedWords):
           # print("Bruh you already guessed it fracaso")
            #continue
        return guess

def Ronda(hipAr):
     hipWord = hipAr[0]
     lengthOfWord = len(hipWord)
        
  
     answeLine = ""
     
     for letra in correctWords:
         hipWord.index(letra)
         
         correctIndex.append(hipWord.index(letra))
         print(correctIndex)
        
     for x in range(lengthOfWord):

        if(x in correctIndex):
         answeLine = answeLine + f"_{list(hipWord)[x]}__   "
        else:
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
     print(hipWord)    
     guess = getInput()
     
     hipLetters = list(hipWord)
     print(hipLetters)
     for letter in hipLetters:
                
                if(guess == letter ):
                    time.sleep(2)
                    correct = True
                   
                   
                    
                    
                    break
                else:
                   
                   correct = False

                   
    
     guessedWords.append(guess)
     if(correct):
            print("You guessed rigth")
            correctWords.append(guess)
     else:
            print("You guessed wrong")
            guessedWrong = guess

 
     count = 0       
     
     
     
     if len(hipWord)==len(correctWords) :
         finished = True
     else :
         finished = False
    

     




def StartGame(hipAr):
    welcome = input("Welcome to my super hipster hangman game?Wanna play?")
    if(welcome == "yes"):
        print("lets get started!!")
        time.sleep(1)
        for j in range(0,100):
            Ronda(hipAr)
            if len(hipWord)==len(correctWords) :
                 break
            
            
             
        print("game done")


    

       
           
    else:
        print("awww")



StartGame(hipAr)


