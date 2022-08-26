
import DirStorage as storage, pygame
from Screen import X, Y, screen



black = (0,0,0)
white = (255,255,255)

class Gamestate():
    def howTo():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("hi")
                #text
                font = pygame.font.Font('Lime Days.ttf', 30)
            titleFont = pygame.font.Font('Lime Days.ttf', 60)

            titleText = titleFont.render("Stack'Em", True, white)
            titleRect = titleText.get_rect()
            screen.blit(titleText, ((X/2)-(titleRect[2]/2), 10))

            player1Text = titleFont.render("Player 1", True, white)
            player1TextRect = player1Text.get_rect()
            screen.blit(player1Text, ((X/4)-(player1TextRect[2]/2), 520))


            player2Text = titleFont.render("Player 2", True, white)
            player2TextRect = player2Text.get_rect()
            screen.blit(player2Text, ((X/4)*(3)-(player2TextRect[2]/2), 520))

            #seperaters
            horizontalTopLine = pygame.draw.line(screen, white, (0, 100), (1390, 100), 5)
            horizontalBottomLine = pygame.draw.line(screen, white, (0, 500), (1390, 500), 5)
            verticalLine = pygame.draw.line(screen, white, (640, 500), (640, 900), 5)



            #gets directions
            for i in range(len(storage.p1)):
                dir = storage.p1[i]
                screen.blit(font.render(dir, True, white), (20, 600 + (i * 40)))
            for i in range(len(storage.p2)):
                dir = storage.p2[i]
                screen.blit(font.render(dir, True, white), (660, 600 + (i * 40)))
                    

                    
