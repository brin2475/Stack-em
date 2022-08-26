# import time, pygame, DirStorage as storage, sys, time
# import Main





# pygame.init()

# #main variables
# minTime = 0
# timerOn =True
# player1Leave = False
# player2Leave = False





# #Screen Setup


# # #text
# # font = pygame.font.Font('Lime Days.ttf', 30)
# # titleFont = pygame.font.Font('Lime Days.ttf', 60)

# # titleText = titleFont.render("Stack'Em", True, white)
# # titleRect = titleText.get_rect()
# # screen.blit(titleText, ((X/2)-(titleRect[2]/2), 10))

# # player1Text = titleFont.render("Player 1", True, white)
# # player1TextRect = player1Text.get_rect()
# # screen.blit(player1Text, ((X/4)-(player1TextRect[2]/2), 520))


# # player2Text = titleFont.render("Player 2", True, white)
# # player2TextRect = player2Text.get_rect()
# # screen.blit(player2Text, ((X/4)*(3)-(player2TextRect[2]/2), 520))

# # #seperaters
# # horizontalTopLine = pygame.draw.line(screen, white, (0, 100), (1390, 100), 5)
# # horizontalBottomLine = pygame.draw.line(screen, white, (0, 500), (1390, 500), 5)
# # verticalLine = pygame.draw.line(screen, white, (640, 500), (640, 900), 5)



# # #gets directions
# # for i in range(len(storage.p1)):
# #     dir = storage.p1[i]
# #     screen.blit(font.render(dir, True, white), (20, 600 + (i * 40)))
# # for i in range(len(storage.p2)):
# #     dir = storage.p2[i]
# #     screen.blit(font.render(dir, True, white), (660, 600 + (i * 40)))


# #updates the screen




# nice = pygame.USEREVENT + 0
# # game loop
# milTime = minTime * 60000
# running = True
# time = pygame.time.set_timer(nice, milTime)
# while running:
#     Main.Gamestate.howTo
    
# # for loop through the event queue  
#     for event in pygame.event.get():
#         if event.type == nice:
#             print("nice")
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_q:
#                 player1Leave = not player1Leave
#             if event.key == pygame.K_o:
#                 player2Leave = not player2Leave
            
            

#             # Check for QUIT event  
#         if (event.type == pygame.QUIT) or (player1Leave and player2Leave) or (timerOn == False):
#             running = False
#             pygame.quit()
#             sys.exit()
        







