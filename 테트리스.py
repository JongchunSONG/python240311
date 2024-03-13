import pygame
import sys
import random
import time

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

# 이전 블록들을 저장하는 리스트
blocks = []

# 게임 루프
clock = pygame.time.Clock()
fall_time = 0.2
last_fall_time = time.time()

def draw_block(x, y, shape, color):
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, color, (x + j * block_size, y + i * block_size, block_size, block_size))

def check_collision(x, y, shape):
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell:
                if x + j * block_size < 0 or x + j * block_size >= width or y + i * block_size >= height:
                    return True
                for old_block in blocks:
                    if old_block['x'] == x + j * block_size and old_block['y'] == y + i * block_size:
                        return True
    return False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 블록 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and block_x > 0 and not check_collision(block_x - block_size, block_y, current_shape):
        block_x -= block_size
    if keys[pygame.K_RIGHT] and block_x < width - block_size * len(current_shape[0]) and not check_collision(block_x + block_size, block_y, current_shape):
        block_x += block_size

    # 블록 회전
    if keys[pygame.K_UP]:
        rotated_shape = list(zip(*current_shape[::-1]))  # 시계방향으로 90도 회전
        if not check_collision(block_x, block_y, rotated_shape):
            current_shape = rotated_shape

    # 아래로 이동
    if keys[pygame.K_DOWN] or time.time() - last_fall_time >= fall_time:
        if block_y < height - block_size * len(current_shape) and not check_collision(block_x, block_y + block_size, current_shape):
            block_y += block_size
            last_fall_time = time.time()
        else:
            blocks.append({'shape': current_shape, 'color': current_color, 'x': block_x, 'y': block_y})
            block_y = 0
            block_x = width // 2
            current_shape = random.choice(shapes)
            current_color = random.choice([cyan, blue, orange, yellow, green, purple, red])

            # 블록이 한 줄 이상이면 삭제
            for i in range(height // block_size):
                row_blocks = [block for block in blocks if block['y'] == i * block_size]
                if len(row_blocks) == width // block_size:
                    blocks = [block for block in blocks if block['y'] != i * block_size]
                    for b in blocks:
                        if b['y'] < i * block_size:
                            b['y'] += block_size

    # 화면 그리기
    screen.fill(black)

    # 이전 블록들 그리기
    for old_block in blocks:
        draw_block(old_block['x'], old_block['y'], old_block['shape'], old_block['color'])

    # 현재 블록 그리기
    draw_block(block_x, block_y, current_shape, current_color)

    pygame.display.flip()

    # 초당 프레임 설정
    clock.tick(30)  # 초당 30프레임으로 설정 (수정 가능)
