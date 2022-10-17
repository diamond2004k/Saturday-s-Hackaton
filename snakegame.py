import pygame
import time
import random

pygame.init()  # Initializing pygame!

WIDTH = 800     # Setting Width and Height for
HEIGHT = 600    # the screen


# Create a display, and set it's height and width.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

# Make into a function
def main_menu():
    
    WIDTH = 800
    HEIGHT = 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake Game')
    
    

def game_over():
    pass
    


def snake_game():
        
    # Create a variable for whether the loop is running or not.
    running = True

    # Start creating Mr. Snake!
    # Create the point where the body of Mr. Snake will start, and what direction it will be going
    snake_pos = [200, 70]
    snake_body = [[200, 70], [200-10, 70], [200-(2*10), 70],[200-(3*10), 70],[200-(4*10), 70],[200-(5*10), 70],[200-(6*10), 70]]
    direction = 'right'
    
    fruit_pos = [0,0]
    create_fruit = True

    score = 0   
    # Create a timer/fps tracker for smooth gameplay
    timer = pygame.time.Clock()
# Start a main game loop.
    while running:
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                running = False
        

        # Get te keys pressed and check which one has been pressed.
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_w] or keys[pygame.K_UP]) and direction != 'down':
                direction = 'up'
            if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and direction != 'up':
                direction = 'down'
            if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and direction != 'left':
                direction = 'right'
            if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and direction != 'right':
                direction = 'left'

        # FIlling in the screen with full black.
        screen.fill((0, 0, 0))
        #fruit generation
        


        # Rendering each part of the snake body instead of just his head.
        for part in snake_body:
            pygame.draw.rect(screen, (255, 255, 0), (part[0], part[1], 10, 10))

    # Change the direction where Mr. Snake is headed.
        if direction == 'right':
            snake_pos[0] += 10
        elif direction == 'left':
            snake_pos[0] -= 10
        elif direction == 'up':
            snake_pos[1] -= 10
        elif direction == 'down':
            snake_pos[1] += 10

        
        snake_body.append(list(snake_pos))

        if create_fruit is True:
            fruit_pos = [random.randint(50,WIDTH - 50),random.randint(50,HEIGHT-50)]
            create_fruit = False 
        pygame.draw.rect(screen, (0,255,0), (fruit_pos[0],fruit_pos[1],10,10))

        if pygame.Rect(snake_pos[0],snake_pos[1],10,10).colliderect(pygame.Rect(fruit_pos[0],fruit_pos[1],10,10)):
            create_fruit = True
            score = score + 1
        else:
            snake_body.pop(0)

        for block in snake_body[:-1]:
            if pygame.Rect(snake_pos[0],snake_pos[1],10,10).colliderect(pygame.Rect(block[0],block[1],10, 10)):
                pygame.quit()
        
        if((snake_pos)[0]  >800 or snake_pos[0]<0):
            pygame.quit()
        if((snake_pos)[1]  >600) or (snake_pos[1]<0):
            pygame.quit()               
        pygame.display.update()
        timer.tick(30)
        
    pygame.quit()

snake_game()
