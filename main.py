import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Константы
WIN_SIZE = (800, 600)
CELL_SIZE = 20
FPS = 10

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Создание игрового окна
window = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption('Змейка')

# Таймер для обновления экрана
clock = pygame.time.Clock()

# Класс для создания змейки
class Snake:
    def __init__(self, color, keys):
        self.color = color
        self.keys = keys
        self.direction = 'RIGHT'
        self.body = [[100, 100], [80, 100], [60, 100]]
        self.score = 0

    def change_direction(self, new_direction):
        if new_direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'
        if new_direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if new_direction == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if new_direction == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'

    def move(self):
        head = list(self.body[0])
        if self.direction == 'RIGHT':
            head[0] += CELL_SIZE
        if self.direction == 'LEFT':
            head[0] -= CELL_SIZE
        if self.direction == 'UP':
            head[1] -= CELL_SIZE
        if self.direction == 'DOWN':
            head[1] += CELL_SIZE
        self.body.insert(0, head)
        if head == food.position:
            self.score += 1
            return True
        else:
            self.body.pop()
            return False

    def draw(self):
        for block in self.body:
            pygame.draw.rect(window, self.color, (*block, CELL_SIZE, CELL_SIZE))

# Класс для создания еды
class Food:
    def __init__(self):
        self.position = [random.randrange(0, WIN_SIZE[0], CELL_SIZE),
                         random.randrange(0, WIN_SIZE[1], CELL_SIZE)]

    def draw(self):
        pygame.draw.ellipse(window, RED, (*self.position, CELL_SIZE, CELL_SIZE))

# Создание змеек
snake1 = Snake(GREEN, [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d])
snake2 = Snake(WHITE, [pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT])

food = Food()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            for i in range(4):
                if event.key == snake1.keys[i]:
                    snake1.change_direction(['UP', 'LEFT', 'DOWN', 'RIGHT'][i])
                if event.key == snake2.keys[i]:
                    snake2.change_direction(['UP', 'LEFT', 'DOWN', 'RIGHT'][i])

    if not snake1.move() or not snake2.move():
        pygame.quit()
        sys.exit()

    if snake1.body[0] in snake2.body or snake2.body[0] in snake1.body:
        pygame.quit()
        sys.exit()

    window.fill((0, 0, 0))
    snake1.draw()
    snake2.draw()
    food.draw()

    pygame.display.update()
    clock.tick(FPS)
