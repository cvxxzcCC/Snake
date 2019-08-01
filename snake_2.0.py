
class Point:
    row = 0
    col = 0

    def __init__(self,row,col):
        self.x = row
        self.y = col

    def copy(self):
        return Point(row = self.x , col = self.y)

import pygame
import socket

import sys
import random

from pygame.locals import *

WindowsColor = pygame.Color(255,0,0)
FoodColor = pygame.Color(255 ,255 ,255)
SnakeColor = pygame.Color(0,0,0)

def dead():
    print("YOU ARE DEAD")
    pygame.quit()
    sys.exit()

def main():
    pygame.init()

    clock = pygame.time.Clock()
    W = 600
    H = 600
    size = (W,H)

    row = 40
    col = 40

    window = pygame.display.set_mode(size)
    pygame.display.set_caption('The Snake Game ! DAZE')

    head = Point(int(row/2),int(col/2))
    headColor = SnakeColor

    SnakeBody=[
        Point(row = head.x , col = head.y+1),
        Point(row = head.x , col = head.y+2),
        Point(row = head.x , col = head.y+3)
    ]

    def getfood():
        while 1:
            foodpostion = Point(row = random.randint(0, row - 1), col = random.randint(0, col - 1))
            is_coll = False

            if foodpostion.x == head.x and foodpostion.y == head.y:
                is_coll = True

            for snake in SnakeBody:
                if foodpostion.x == snake.x and foodpostion.y == snake.y:
                    is_coll = True
                    break

            if not is_coll:
                break

        return foodpostion

    food = getfood()
    print(food.x)
    print(food.y)
    foodflag = 0

    def rect(Point,color):
        left = Point.x * ( W/row )
        top =  Point.y * ( H/col )
        pygame.draw.rect(
            window,
            color,
            (left , top , W/row , H/col)
        )

    diraction = 'right'
    changediraction = 'right'

    quit = True

    while (quit):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = False

            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    changediraction = 'right'
                if event.key == K_LEFT:
                    changediraction = 'left'
                if event.key == K_DOWN:
                    changediraction = 'down'
                if event.key == K_UP:
                    changediraction = 'up'
                if event.key == K_ESCAPE:
                    quit == False

        if changediraction == 'right' and diraction != 'left':
            diraction = changediraction
        if changediraction == 'left' and diraction != 'right':
            diraction = changediraction
        if changediraction == 'down' and diraction != 'up':
            diraction = changediraction
        if changediraction == 'up' and diraction != 'down':
            diraction = changediraction


        SnakeBody.insert(0, head.copy())

        if head.x == food.x and head.y == food.y:
            foodflag = 1
        else:
            SnakeBody.pop()

        if foodflag == 1:
            foodflag = 0
            food = getfood()


        if diraction == 'right':
            head.x += 1
        if diraction == 'left':
            head.x -= 1
        if diraction == 'up':
            head.y -= 1
        if diraction == 'down':
            head.y += 1

        death = False
        if head.x < 0 or head.y < 0 or head.y > col or head.x > row:
            death = True

        for snake in SnakeBody:
            if snake.x == head.x and snake.y == head.y:
                death =True
                break

        if death :
            dead()

        pygame.draw.rect(
            window,
            WindowsColor,
            (0,0,W,H)
        )

        rect(head , headColor)
        rect(food , FoodColor)
        for snake in SnakeBody:
            rect(snake , headColor)


        pygame.display.flip()

        clock.tick(10)



if __name__ == '__main__':
    main()
