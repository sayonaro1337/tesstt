import pygame
import random

pygame.init()

# Инициализация размеров окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Собери все кристаллы!")

# Определение цветов
WHITE = (255, 255, 255)

# Загрузка изображений
player_image = pygame.image.load('femalePerson_walk4.png')


crystal_image = pygame.image.load('gemRed.png')


spike_image = pygame.image.load('cactus.png')


# Начальные позиции игрока
player_pos = [WIDTH // 2, HEIGHT // 2]
velocity = 5

# Генерация позиций кристаллов
crystals = [[random.randint(0, WIDTH - 20), random.randint(0, HEIGHT - 20)] for _ in range(5)]
score = 0

# Генерация позиций шипов
spikes = [[random.randint(0, WIDTH - 30), random.randint(0, HEIGHT - 30)] for _ in range(5)]

# Шрифты для отображения счета
font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= velocity
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - 50:
        player_pos[0] += velocity
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= velocity
    if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - 50:
        player_pos[1] += velocity

    for crystal in crystals[:]:
        if (player_pos[0] < crystal[0] + 20 and
            player_pos[0] + 50 > crystal[0] and
            player_pos[1] < crystal[1] + 20 and
            player_pos[1] + 50 > crystal[1]):
            crystals.remove(crystal)
            score += 1

    for spike in spikes:
        if (player_pos[0] < spike[0] + 30 and
            player_pos[0] + 50 > spike[0] and
            player_pos[1] < spike[1] + 30 and
            player_pos[1] + 50 > spike[1]):
            running = False  

    # Рисуем игрока
    screen.blit(player_image, player_pos)

    # Рисуем кристаллы
    for crystal in crystals:
        screen.blit(crystal_image, crystal)

    # Рисуем шипы
    for spike in spikes:
        screen.blit(spike_image, spike)

    if not crystals:
        text = font.render("Все кристаллы собраны!", True, (0, 0, 0))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))

    score_text = font.render(f"Счёт: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
