
import pygame# imports the Library used for the display
import time# imports time module
import random# imports the random mocule thet alows for randomising numbers

 
pygame.init() #Starts all the modules used for the game
 
 
white = (255, 255, 255)# defines the rgb for white
black = (0, 0, 0)# defines the rgb for black
red = (255, 0, 0)# defines the rgb for red
blue = (0, 0, 255)# defines the rgb for blue
 
dis_width = 800# defines the width of display
dis_height  = 600# defines the heigth of display
 
dis = pygame.display.set_mode((dis_width, dis_width))#Opens the display and sets the bounderies for it
pygame.display.set_caption('Snake game by Carlos Q')#Starts the caption for the game
 
game_over = False# the variable game over is defined as False
clock = pygame.time.Clock()#the velocity of the game is defined
 
snake_block = 10
snake_speed = 30
 
font_style = pygame.font.SysFont(None, 30)# sets the font size to 50
 
 
def message(msg,color):# creates a function calles message that takes in a message and color
    mesg = font_style.render(msg, True, color)#renders in the message
    dis.blit(mesg, [dis_width/3, dis_height/3])# sets the location of the messafe to the middle
 
 
def gameLoop():  # creating a function
    game_over = False# game over is defined as false
    game_close = False# game close is defined as false
 
    x1 = dis_width / 2# the middle of the display is defined
    y1 = dis_height / 2
 
    x1_change = 0# the x change of the snake is 0
    y1_change = 0# the y change of the snake is 0
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
 
    while not game_over:#code belows loops while the game is not over
 
        while game_close == True:#If the game is closed
            dis.fill(white)# fill the screen white
            message("You Lost! Press Q-Quit or C-Play Again", red)# display the message in red
            pygame.display.update()# update the display
 
            for event in pygame.event.get():# for every event in the game
                if event.type == pygame.KEYDOWN:# if a key is pressed
                    if event.key == pygame.K_q:# if the key is q quit the game
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:# if the key is c play again
                        gameLoop()# call the function for the game again
 
        for event in pygame.event.get():# for every event in the game
            if event.type == pygame.QUIT:#if thhe exit button is pressed
                game_over = True# quit the game
            if event.type == pygame.KEYDOWN:# if a key is pressed
                if event.key == pygame.K_LEFT:#check if the key is the left
                    x1_change = -snake_block #change the x value of the snake negative 
                    y1_change = 0 # dont change the y value
                elif event.key == pygame.K_RIGHT: #check if the key is the rigth
                    x1_change = snake_block #change the x value of the snake positively
                    y1_change = 0 # dont change the y value
                elif event.key == pygame.K_UP: #check if the key is the up
                    y1_change = -snake_block #change the y value of the snake negative 
                    x1_change = 0#dont change the x value
                elif event.key == pygame.K_DOWN: #check if the key pressed is down
                    y1_change = snake_block# change the y value of the snake positevely 
                    x1_change = 0# doent change the x value
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: #if you hit the 
            game_close = True #game is over
 
        x1 += x1_change#the x value of the rectangle is aded to the change in x vale defined
        y1 += y1_change#the y value of the rectangle is aded to the change in y vale defined
        dis.fill(white)# background is filled white
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        pygame.display.update()# updates the display
 
        if x1 == foodx and y1 == foody: # if the snake touches the food
            print("Yummy!!") #prints Yummy
        clock.tick(snake_speed) # make the game run at this velocity
 
    pygame.quit() # quit the game
    quit() # quit the code
 
 
gameLoop() 