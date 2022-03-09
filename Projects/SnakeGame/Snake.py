
import pygame# imports the Library used for the display
pygame.init() #Starts all the modules used for the game
dis=pygame.display.set_mode((400,300))#Opens the display and sets the bounderies for it
pygame.display.update()# updates the display (usless for now)
pygame.display.set_caption('Snake game by Carlos Q')#Sts the caption for the game
game_over=False #Creates a variable to make th
while not game_over:#Whie game not over do whats below
    for event in pygame.event.get(): #for every event in the game
        print(event)   #prints out all the actions that take place on the screen
 
pygame.quit()#quits the display
quit()#quit the code as a whole