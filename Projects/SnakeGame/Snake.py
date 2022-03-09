

import pygame# imports the Library used for the display
import time# imports time module
pygame.init() #Starts all the modules used for the game
 
white = (255, 255, 255)# defines the rgb for white
black = (0, 0, 0)# defines the rgb for black
red = (255, 0, 0)# defines the rgb for red
  
dis_width = 800# defines the width of display
dis_height  = 600# defines the heigth of display
dis = pygame.display.set_mode((dis_width, dis_width))#Opens the display and sets the bounderies for it
pygame.display.set_caption('Snake game by Carlos Q')#Starts the caption for the game
 
game_over = False
 
x1 = dis_width/2#sets the original x value for our rectangle to the middle of the screen
y1 = dis_height/2#sets the original y value for our rectangle to the  middle of the rectangle
 
x1_change = 0# defines the change in x as none( technically zero but you understand)       
y1_change = 0# defines the change in y as none( technically zero but you understand)       
 
clock = pygame.time.Clock()# defines the velocity of the game
 

font_style = pygame.font.SysFont(None, 50)# sets the font size to 50

 
def message(msg,color):# creates a function calles message that takes in a message and color
    mesg = font_style.render(msg, True, color)#renders in the message
    dis.blit(mesg, [dis_width/2, dis_height/2])# sets the location of the messafe to the middle
while not game_over:#Whie game not over do whats below
    for event in pygame.event.get():
        if event.type == pygame.QUIT:# if the quit button is clicked
            game_over = True# game over 
        if event.type == pygame.KEYDOWN:# if a key is pressed
            if event.key == pygame.K_LEFT:#check if the key is the left
                x1_change = -10 # change x by -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:#check if the key is the ritgt
                x1_change = 10# change x by 10
                y1_change = 0
            elif event.key == pygame.K_UP:#check if the key is up
                y1_change = -10# change y by -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:#check if the key is down
                y1_change = 10# change y by 10
                x1_change = 0
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: #if you hit the border
        game_over = True# game is over
    x1 += x1_change#the x value of the rectangle is aded to the change in x vale defined
    y1 += y1_change#the y value of the rectangle is aded to the change in y vale defined
    dis.fill(white)# background is filled white
    pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])# create the rectnge with the values
 
    pygame.display.update()# update the display
 
    clock.tick(30)#set the game velocity to 30 tiks
 
pygame.quit()# quit the game
quit()# quit the code




