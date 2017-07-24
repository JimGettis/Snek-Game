import pygame, time, random
from scripts.UltraColor import *


pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Snek Game")

icon = pygame.image.load("graphics//apple.png")
pygame.display.set_icon(icon)

img = pygame.image.load("graphics//snakehead.png")
appleimg = pygame.image.load("graphics//apple.png")

clock = pygame.time.Clock()

AppleThickness = 30
block_size = 20
FPS = 15

direction = "right"

smallfont = pygame.font.SysFont("constantia", 25)
medfont = pygame.font.SysFont("constantia", 45)
largefont = pygame.font.SysFont("constantia", 70)



def pause():

    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(Color.Black)
        message_to_screen("PAUSED", Color.White, -100, size = "large")
        message_to_screen("Press C to continue or Q to quit", Color.White, 25)
        pygame.display.update()
        clock.tick(5)

def score(score):
    text = smallfont.render("Score: " +str(score), True, Color.Black)
    gameDisplay.blit(text, [600, 0])


def randAppleGen():
    randAppleX = round(random.randrange(0, display_width - AppleThickness) / 10.0) * 10
    randAppleY = round(random.randrange(0, display_height - AppleThickness) / 10.0) * 10

    return randAppleX, randAppleY


def game_intro():
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_c:
                    intro = False



        gameDisplay.fill(Color.DarkSeaGreen)
        message_to_screen("Welcome to Snek Game", Color.Green, -100, "large")
        message_to_screen("The objective of the game is to eat the apples", Color.Purple, -30)
        message_to_screen("The more apples you eat the longer you get", Color.Purple, 10)
        message_to_screen("If you run into yourself or the edges, you die", Color.Purple, 50)
        message_to_screen("Press C to play, P to pause or Q to quit.", Color.DarkSlateBlue, 150)
        pygame.display.update()
        clock.tick(10)


def snake(block_size, snakeList):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img, 180)

    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))


    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, Color.Green, [XnY[0], XnY[1], block_size, block_size])


def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)






#MAIN GAME LOOP
def gameLoop():
    global direction
    gameExit = False
    gameOver = False

    direction = "right"

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX, randAppleY = randAppleGen()

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(Color.Black)
            message_to_screen("GAME OVER!!", Color.Red, y_displace = -15, size = "large")
            message_to_screen("Press C to play again or Q to quit", Color.White, y_displace = 60, size = "medium")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            # MOVEMENT EVENTS
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    direction = "up"
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    direction = "down"
                    lead_y_change = - block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()
        #BOUNDARIES
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0 :
            gameOver = True


        lead_x += lead_x_change
        lead_y -= lead_y_change


        # RENDER DISPLAY
        gameDisplay.fill(Color.DarkSeaGreen)
#        pygame.draw.rect(gameDisplay, Color.Red, [randAppleX, randAppleY, AppleThickness, AppleThickness])

        gameDisplay.blit(appleimg, (randAppleX, randAppleY))
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList)

        score((snakeLength - 1) * 100)

        pygame.display.update()

        #EATING THE APPLE

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1


            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1




        clock.tick(FPS)



    pygame.quit()
    quit()

game_intro()
gameLoop()
