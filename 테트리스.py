import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 설정
width, height = 300, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("테트리스")

# 색깔 정의
black = (0, 0, 0)
white = (255, 255, 255)
cyan = (0, 255, 255)
blue = (0, 0, 255)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 128, 0)
purple = (128, 0, 128)
red = (255, 0, 0)

# 테트리스 블록 모양 정의
shapes = [
    [[1, 1, 1, 1]],
    [[1, 1, 1], [1]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 1], [0, 1]],
    [[1, 1, 1], [1, 0]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1], [1, 1]]
]

# 블록 크기 및 초기 위치
block_size = 30
block_x, block_y = width // 2, 0

# 현재 블록과 색상 설정
current_shape = random.choice(shapes)
current_color = random.choice([cyan, blue, orange, yellow, green, purple, red])

# 게임 루프
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 블록 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and block_x > 0:
        block_x -= block_size
    if keys[pygame.K_RIGHT] and block_x < width - block_size * len(current_shape[0]):
        block_x += block_size
    if keys[pygame.K_DOWN] and block_y < height - block_size * len(current_shape):
        block_y += block_size

    # 화면 그리기
    screen.fill(black)

    # 현재 블록 그리기
    for i, row in enumerate(current_shape):
        for j, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, current_color, (block_x + j * block_size, block_y + i * block_size, block_size, block_size))

    # 블록이 바닥에 닿으면 새로운 블록 생성
    if block_y >= height - block_size * len(current_shape):
        block_y = 0
        block_x = width // 2
        current_shape = random.choice(shapes)
        current_color = random.choice([cyan, blue, orange, yellow, green, purple, red])

    pygame.display.flip()

    # 초당 프레임 설정
    clock.tick(5)  # 초당 5프레임으로 설정 (수정 가능)
