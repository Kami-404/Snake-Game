import pygame
import random

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
width, height = 600, 400

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

speed = 15
snake_x = width // 2
snake_y = height // 2
snake_size = 10
x_change = 0
y_change = 0
snake_list = []
snake_length = 1

def text_screen(text, color, x, y):
    font = pygame.font.Font(None, 30)
    screen_text = font.render(text, True, color)
    window.blit(screen_text, [x, y])

food_x = random.randint(0, (width - snake_size) // snake_size) * snake_size
food_y = random.randint(0, (height - snake_size) // snake_size) * snake_size

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -snake_size
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = snake_size
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = -snake_size
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = snake_size

    snake_x += x_change
    snake_y += y_change

    if snake_x >= width or snake_x < 0 or snake_y >= height or snake_y < 0:
        game_over = True

    window.fill(white)

    for segment in snake_list:
        pygame.draw.rect(window, green, [segment[0], segment[1], snake_size, snake_size])

    snake_head = [snake_x, snake_y]
    snake_list.append(snake_head)

    if len(snake_list) > snake_length:
        del snake_list[0]

    for block in snake_list[:-1]:
        if block == snake_head:
            game_over = True

    if snake_x == food_x and snake_y == food_y:
        food_x = random.randint(0, (width - snake_size) // snake_size) * snake_size
        food_y = random.randint(0, (height - snake_size) // snake_size) * snake_size
        snake_length += 1

    pygame.draw.rect(window, red, [food_x, food_y, snake_size, snake_size])
    pygame.display.update()

    pygame.time.Clock().tick(speed)

pygame.quit()
quit()