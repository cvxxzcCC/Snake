
import pygame, sys, random
# pygame所使用的常量
from pygame.locals import *

RedColor = pygame.Color(255, 0, 0)
BlackColor = pygame.Color(0, 0, 0)
WhiteColor = pygame.Color(255, 255, 255)

# 2，定义游戏结束函数
def gameOver():
    pygame.quit()
    sys.exit()


# 3，定义main函数
def main():
    pygame.init()
    fpsClock = pygame.time.Clock()
    playSurface = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('贪吃蛇')

    snakePosition = [100, 100]
    snakeBody = [[100, 100], [80, 100], [60, 100]]

    targetPosition = [300, 200]
    Targetflag = 1

    direction = 'right'
    ChangeDirection = direction

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    ChangeDirection = 'right'
                if event.key == K_LEFT:
                    ChangeDirection = 'left'
                if event.key == K_UP:
                    ChangeDirection = 'up'
                if event.key == K_DOWN:
                    ChangeDirection  = 'down'
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

        if ChangeDirection == 'left' and not direction == 'right':
            direction = ChangeDirection
        if ChangeDirection == 'right' and not direction == 'left':
            direction = ChangeDirection
        if ChangeDirection == 'up' and not direction == 'down':
            direction = ChangeDirection
        if ChangeDirection == 'down' and not direction == 'up':
            direction = ChangeDirection


        if direction == 'right':
            snakePosition[0] += 20
        if direction == 'left':
            snakePosition[0] -= 20
        if direction == 'up':
            snakePosition[1] -= 20
        if direction == 'down':
            snakePosition[1] += 20

        #保证身体在前进，为了防止身体一直增长，后面有pop让他保持尾巴减少
        snakeBody.insert(0, list(snakePosition))

        if snakePosition[0] == targetPosition[0] and snakePosition[1] == targetPosition[1]:
            Targetflag = 0
        #else 一旦删除，长度会一直变长，每前进一格 要pop出去尾巴
        else:
            snakeBody.pop()

        if Targetflag == 0:
            x = random.randrange(1, 31)
            y = random.randrange(1, 23)
            targetPosition = [int(x * 20), int(y * 20)]

            Targetflag = 1

        #画出画面，之前都是数据，将事物图像化

        #画出屏幕，如果去掉，就相当于在 透明画布上涂颜色（默认黑色为透明色）
        #需要每一次都有随着更新只显示一个蛇
        playSurface.fill(BlackColor)

        for position in snakeBody:
            pygame.draw.rect(playSurface, WhiteColor, Rect(position[0], position[1], 20, 20))
            pygame.draw.rect(playSurface, RedColor, Rect(targetPosition[0], targetPosition[1], 20, 20))
            # 第一个参数surface:指定一个编辑区
            # 第二个参数color:颜色
            # 第三个参数填充 Rect:返回矩形(（x,y）,(width,height))
            # 第四个参数width:表示线条粗细 width=0 填充
            # width=1 实心

            pygame.display.flip()

            if snakePosition[0] > 620 or snakePosition[0] < 0:
                gameOver()
            elif snakePosition[1] > 460 or snakePosition[1] < 0:
                gameOver()

            fpsClock.tick(40)

if __name__ == '__main__':
    main()
