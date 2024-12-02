import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
turquoise = (64, 224, 208)
light_green = (144, 238, 144)

score = 0 

width = 1920
height = 1080
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Змейка')

clock = pygame.time.Clock()

snake_block = 20 
snake_speed = 10

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def file_read():  # Чтение
    with open(r"C:\Users\as7\Desktop\лидер.txt", "r") as file:
        data = file.read()
    print("Текст в файле: ", data)

def file_rewrite(user_name, score):  # Перезапись
    with open(r"C:\Users\as7\Desktop\лидер.txt", "w") as file: 
        file.write(f"{user_name}, {score}\n")  # Записываем имя пользователя и результат
    file_read()

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, turquoise, [x[0], x[1], snake_block, snake_block]) 

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

def display_game_over_image():
    game_over_image = pygame.image.load(r"C:\Users\as7\Desktop\bigname1.jpg")
    game_over_image = pygame.transform.scale(game_over_image, (width, height))
    screen.blit(game_over_image, (0, 0))
    pygame.display.update() 

def get_username():
    input_active = True
    user_name = ''
    
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:  
                    user_name = user_name[:-1]
                else:
                    user_name += event.unicode 

        screen.fill(white) 
        name_surface = font_style.render("Введите ваше имя: " + user_name, True, black)
        screen.blit(name_surface, [width / 6, height / 3])
        pygame.display.update()

    return user_name

# Главный игровой цикл
def gameLoop(user_name): 
    game_over = False
    game_close = False
    score = 0
    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    background_image = pygame.image.load(r"C:\Users\as7\Desktop\bigname.jpg")  
    background_image = pygame.transform.scale(background_image, (width, height)) 

    while not game_over:

        while game_close:
            display_game_over_image()
            message(f"{user_name}, ты проиграл! Q - выйти или C - играть заново", black)
            file_rewrite(user_name, score)  # Передаем имя и результат

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop(user_name)

            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        
        screen.blit(background_image, (0, 0))
        
        pygame.draw.rect(screen, light_green, [foodx, foody, snake_block, snake_block])  
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

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1
            score += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

user_name = get_username()
gameLoop(user_name)
