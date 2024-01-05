import pygame
import sys

# 初始化Pygame
pygame.init()

# 設定遊戲窗口
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("擬真賽車遊戲")

# 定義顏色
white = (255, 255, 255)
black = (0, 0, 0)

# 賽車初始位置和速度
car_x = width // 2
car_y = height - 100
car_speed = 5

# 主遊戲迴圈
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < width - 50:
        car_x += car_speed

    # 清空屏幕
    screen.fill(white)

    # 繪製賽車
    pygame.draw.rect(screen, black, (car_x, car_y, 50, 80))

    # 更新顯示
    pygame.display.flip()

    # 控制遊戲迴圈的速度
    pygame.time.Clock().tick(60)
