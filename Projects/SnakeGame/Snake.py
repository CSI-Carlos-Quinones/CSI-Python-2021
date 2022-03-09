

import pygame# imports the Library used for the display
pygame.init() #Starts all the modules used for the game
 
white = (255, 255, 255)# defines the rgb for white
black = (0, 0, 0)# defines the rgb for black
red = (255, 0, 0)# defines the rgb for red
 
dis = pygame.display.set_mode((800, 600))#Opens the display and sets the bounderies for it
pygame.display.set_caption('Snake game by Carlos Q')#Starts the caption for the game
 
game_over = False
 
x1 = 300#sets the original x value for our rectangle
y1 = 300#sets the original y value for our rectangle
 
x1_change = 0# defines the change in x as none( technically zero but you understand)       
y1_change = 0# defines the change in y as none( technically zero but you understand)       
 
clock = pygame.time.Clock()# defines the velocity of the game
 
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
 
    x1 += x1_change#the x value of the rectangle is aded to the change in x vale defined
    y1 += y1_change#the y value of the rectangle is aded to the change in y vale defined
    dis.fill(white)# background is filled white
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])# create the rectnge with the values
 
    pygame.display.update()# update the display
 
    clock.tick(30)#set the game velocity to 30 tiks
 
pygame.quit()# quit the game
quit()# quit the code




