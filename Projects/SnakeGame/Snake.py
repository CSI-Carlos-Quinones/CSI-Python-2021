
import pygame# imports the Library used for the display
pygame.init() #Starts all the modules used for the game
dis=pygame.display.set_mode((400,300))#Opens the display and sets the bounderies for it
pygame.display.update()# updates the display (usless for now)
pygame.display.set_caption('Snake game by Carlos Q')#Sts the caption for the game
 
blue=(0,0,255)# defines the rgb for blue
red=(255,0,0)#defines the rgb for red
 
game_over=False #Creates a variable to make th
while not game_over:#Whie game not over do whats below
    for event in pygame.event.get(): #for every event in the game
        if event.type==pygame.QUIT:# is the exit button is pressed
            game_over=True# the game is over
    pygame.draw.rect(dis,blue,[200,150,10,10])# draws a rectange that is blue
    pygame.display.update() # updates the display
pygame.quit()#quits the display
quit()#quit the code as a whole