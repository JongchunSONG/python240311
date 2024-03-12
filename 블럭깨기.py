import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 설정
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("블록 깨기 게임")

# 색깔 정의
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 패들 설정
paddle_width, paddle_height = 300, 20
paddle_x = (width - paddle_width) // 2
paddle_y = height - 20

# 공 설정
ball_radius = 10
ball_x = width // 2
ball_y = height // 2
ball_speed_x = random.choice([-5, 5])
ball_speed_y = -5

# 블록 설정
block_width, block_height = 50, 20
block_rows = 5
block_cols = width // block_width

blocks = []
for row in range(block_rows):
    for col in range(block_cols):
        block_x = col * block_width
        block_y = row * block_height
        blocks.append(pygame.Rect(block_x, block_y, block_width, block_height))

# 게임 루프
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 5
    if keys[pygame.K_RIGHT] and paddle_x < width - paddle_width:
        paddle_x += 5

    # 공 이동
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 벽과 패들 충돌 검사
    if ball_x <= 0 or ball_x >= width:
        ball_speed_x *= -1
    if ball_y <= 0 or (paddle_y <= ball_y <= paddle_y + paddle_height and paddle_x <= ball_x <= paddle_x + paddle_width):
        ball_speed_y *= -1

    # 블록과 공 충돌 검사
    for block in blocks:
        if block.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius)):
            blocks.remove(block)
            ball_speed_y *= -1

    # 화면 그리기
    screen.fill(black)
    pygame.draw.rect(screen, white, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, red, (int(ball_x), int(ball_y)), ball_radius)

    for block in blocks:
        pygame.draw.rect(screen, white, block)

    pygame.display.flip()

    # 초당 프레임 설정
    clock.tick(60)
