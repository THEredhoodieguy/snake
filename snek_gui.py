#written for python 3.0+
#Matthew Pletcher 2017

import pygame

from snek_game import *

#colors used from PICO-8 default pallette
BLACK      = (  0,   0,   0)
DARKBLUE   = ( 29,  43,  83)
DARKPURPLE = (126,  37,  83)
DARKGREEN  = (  0, 135,  81)
BROWN      = (171,  82,  54)
DARKGRAY   = ( 95,  87,  79)
LIGHTGRAY  = (194, 195, 199)
WHITE      = (255, 241, 232)
RED        = (255,   0,  77)
ORANGE     = (255, 163,   0)
YELLOW     = (255, 236,  39)
GREEN      = (  0, 228,  54)
BLUE       = ( 41, 173, 255)
INDIGO     = (131, 118, 156)
PINK       = (255, 119, 168)
PEACH      = (255, 204, 170)

class Snek_Game(object):

    def __init__(self):
        pygame.init()

        width  = 32
        height = 32

        scalar = 30

        count = 0

        game_keeper = GameKeeper(width, height)

        snek = game_keeper.snek

        horizontal_offset = 20
        vertical_offset = 20 + 20

        screen_width  = width * scalar + horizontal_offset
        screen_height = height * scalar + vertical_offset

        WINDOW_SIZE = [screen_width, screen_height]
        screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Super Snek")

        myFont = pygame.font.Font(None, 30)

        clock = pygame.time.Clock()

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                
                #catch buttons being pressed
                if event.type == pygame.KEYDOWN:
                    if game_keeper.gamestate == 1:
                        if event.key == pygame.K_RIGHT:
                            snek.turn_right()
                        if event.key == pygame.K_LEFT:
                            snek.turn_left()
                    if event.key == pygame.K_RETURN and game_keeper.gamestate == 0:
                        game_keeper.start_game()
                    if event.key == pygame.K_RETURN and game_keeper.gamestate == 2:
                        game_keeper.new_game()
                        snek = game_keeper.snek


            count = count % 60

            #draw our screen 
            screen.fill(BLACK)

            tail = snek.tail
            fruits = game_keeper.fruits

            #render the start screen when the gamestate is 0
            if(game_keeper.gamestate == 0):
                text = "Press enter to start"
                ren = myFont.render(text, 0, WHITE)
                screen.blit(ren, (10, 10))

            #render the game when the gamestate is 1
            if(game_keeper.gamestate == 1):
                #draw the snek
                pygame.draw.rect(screen,
                        GREEN,
                        [snek.x * scalar + horizontal_offset//2,
                         snek.y * scalar + (vertical_offset - 10), 
                        scalar, scalar
                        ])
                #draw the snek's tail
                for i in tail:
                    pygame.draw.rect(screen,
                        GREEN,
                        [i[0] * scalar + horizontal_offset//2,
                        i[1] * scalar + (vertical_offset - 10),
                        scalar, scalar
                        ])
                #draw the fruits
                for i in fruits:
                    pygame.draw.rect(screen,
                        RED,
                        [i.x * scalar + horizontal_offset//2,
                        i.y * scalar + (vertical_offset - 10),
                        scalar, scalar
                        ])
                #draw the boundaries
                #top boundary
                pygame.draw.rect(screen,
                    DARKBLUE,
                    [0, vertical_offset - 20, screen_width, 10])
                #bottom boundary
                pygame.draw.rect(screen,
                    DARKBLUE,
                    [0, screen_height - 10, screen_width, 10])
                #left boundary
                pygame.draw.rect(screen,
                    DARKBLUE,
                    [0, vertical_offset - 20, 10, screen_height - (vertical_offset - 20)])
                #right boundary
                pygame.draw.rect(screen,
                    DARKBLUE,
                    [screen_width - 10, vertical_offset - 20, 10, screen_height - (vertical_offset - 20)])

                text = "SCORE:" + str(game_keeper.score)
                ren = myFont.render(text, 0, WHITE)
                screen.blit(ren, (screen_width - 30*scalar, 10))

                if count % 4 == 0:
                    game_keeper.update()

            #render the game over screen when the gamestate is 2
            if(game_keeper.gamestate == 2):
                text1 = "GAME OVER"
                text2 = "Press enter to start again"
                
                ren1 = myFont.render(text1, 0, WHITE)
                ren2 = myFont.render(text2, 0, WHITE)

                screen.blit(ren1, (10, 10))
                screen.blit(ren2, (10, 30))

            clock.tick_busy_loop(60)

            pygame.display.update()

            count += 1

        pygame.quit()