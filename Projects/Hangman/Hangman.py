#Biografia de San Ignacio de Loyola

from multiprocessing.connection import wait
import random
import urllib.request
import json
from xml.sax import parseString
from RandomHipsterStuff import RandomHipsterStuff
import time
import sys 





def delDuplicate(hipAr):
    for word in hipAr:
        string =word
        #print(string)
        #Counts each character present in the string  
        for i in range(0, len(string)):  
            count = 1;  
            
            for j in range(i+1, len(string)):  
                if(string[i] == string[j] and string[i] != ' '):  
                    count = count + 1;  
                    #Set string[j] to 0 to avoid printing visited character  
                    string = string[:j] + '0' + string[j+1:];  
                # print(string)
                # print(f"{string}:{duplicates}")
            
            #A character is considered as duplicate if count is greater than 1  
            if(count > 1 and string[i] != '0'):  
                duplicates.append(string[i])
            else :
                zero.append(string)

    notZero =[]
    for f in zero:
        if("0" not in f):
        
            notZero.append(f)

    for rep in notZero:
        print(f"{len(rep)} : {rep}")
        print(f"{notZero.count(rep)} : {rep}")
        
        if(len(rep)== notZero.count(rep)):
            #print(rep)
            global hipWord
            hipWord = rep
            single = True
            break
    


    #hipWord = hipAr[0]

            
    print(notZero)           
    print(hipAr) 
    print(hipWord)
    if(single != True):
        return False
    if(single==True):
        return single
    #print(duplicates)



def getHips():

    hipUrl = "https://random-data-api.com/api/hipster/random_hipster_stuff?"


    req = urllib.request.Request(hipUrl)
    requestData = json.loads(urllib.request.urlopen(req).read())

    myHipster = RandomHipsterStuff(**requestData)


    hipAr = myHipster.words
    duplicated = delDuplicate(hipAr)
    while duplicated== False:
        getHips()
    return hipWord

count = 0

duplicates = []
duplicateDict={}
duplicateIndex=[]
zero = []
hipWord= getHips()
hipLetters = ""

#print(hipAr)


hipLetters = list(hipWord)
guessedWrong= []
correctIndex=[]

hangedImgAr= [""" 
     _____________
     |/      |
     |      
     |
    _|___
   """,""" 
     _____________
     |/      |
     |      (_)
     |      
     |
    _|___
   """,
   """ 
     _____________
     |/      |
     |      (_)
     |       |
     |       
     |
    _|___
   """,""" 
     _____________
     |/      |
     |      (_)
     |      \|
     |
    _|___
   """,
   """ 
     _____________
     |/      |
     |      (_)
     |      \|/
     |       
     |
    _|___
   """,""" 
     _____________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___
   """,
   """ 
     _____________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___
   """]

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

def Ronda(hipWord):
     
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
           
    
     try:
        print(hangedImgAr[len(guessedWrong)])
     except:
         print("YOU LOST")
         sys.exit()
     print(f"Im thinking of a {lengthOfWord} letter word")
     print(answeLine)
    # print(hipWord)    
     guess = getInput()
     
   
     print(hipLetters)
     for letter in hipLetters:
                
                if(guess == letter ):
                    
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
            guessedWrong.append(guess)

 
     count = 0       
     
     
     
     if len(hipWord)==len(correctWords) :
         finished = True
     else :
         finished = False
 
def StartGame(hipWord):
    welcome = input("Welcome to my super hipster hangman game?Wanna play?")
    if(welcome == "yes"):
        print("lets get started!!")
        #hipWord = getHips()
        for j in range(0,100):
            Ronda(hipWord)
            if len(hipWord)==len(correctWords) :
                 break
            if(len(guessedWrong)== 6):
                print("YOU LOST!")
            
            
             
        print("YOU WINNN!!!!!")


    

       
           
    else:
        print("awww")



StartGame(hipWord)


