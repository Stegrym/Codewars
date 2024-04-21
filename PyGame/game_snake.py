import pygame
import time
import random

# 41,112

pygame.init()
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (130, 0, 0)
green = (0, 130, 0)
blue = (0, 0, 130)
grey = (200, 200, 200)

screen_width_x = 500
screen_height_y = 580

game_screen = pygame.display.set_mode((screen_width_x, screen_height_y))
pygame.display.set_caption('Snake')  # game window name
clock = pygame.time.Clock()

snake_block = 10
snake_speed = 10

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)


def score(score):
    value = score_font.render('points: ' + str(score), True, black)
    game_screen.blit(value, [30, 520])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_screen, green, [
                         x[0], x[1], snake_block, snake_block])


def message(msg, color=black):  # dirty
    text1 = 'Game Over'
    text2 = 'R --> ReStart'
    text3 = 'Q --> Quit'
    mesg1 = font_style.render(text1, True, color, )
    mesg2 = font_style.render(text2, True, color, )
    mesg3 = font_style.render(text3, True, color, )
    game_screen.blit(mesg1, [screen_width_x / 3, screen_height_y / 4])
    game_screen.blit(mesg2, [screen_width_x / 3, screen_height_y / 4 + 100])
    game_screen.blit(mesg3, [screen_width_x / 3, screen_height_y / 4 + 150])


def game_start():
    game_over = False
    game_close = False
    x1 = screen_width_x/2
    y1 = screen_height_y/2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(10, 470)/10)*10
    foody = round(random.randrange(10, 470)/10)*10

    while not game_over:
        while game_close == True:
            game_screen.fill(black)
            message('Looooser!', white)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_start()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    x1_change = 0
                    y1_change = snake_block
        # if x1 >= dis_width_x or x1 < 0 or y1 >= dis_height_y or y1 < 0:  # outside game_box death
        #     game_close = True

        ''' Snake teleport '''
        if x1 == 500.0:
            x1 = 10.0
        if x1 == 0.0:
            x1 = 490.0
        if y1 == 500.0:
            y1 = 10.0
        if y1 == 0.0:
            y1 = 490.0

        x1 += x1_change
        y1 += y1_change
        # print(f'x == {x1}, y == {y1}')  # points
        game_screen.fill(grey)
        pygame.draw.rect(game_screen, red, [
                         foodx, foody, snake_block, snake_block])
        pygame.draw.rect(game_screen, black, [
                         (0, 0), (500, 510)], 20)  # need line
        pygame.draw.rect(game_screen, black, [(0, 0), (500, 580)], 20)
        pygame.display.update()
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        score(Length_of_snake - 1)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(10, 470)/10) * 10
            foody = round(random.randrange(10, 470)/10) * 10
            Length_of_snake += 1
        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_start()
