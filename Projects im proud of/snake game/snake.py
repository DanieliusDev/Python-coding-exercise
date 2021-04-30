import pygame
import os
import random

# initializing game
pygame.init()

# TODO here begins my super awesome SNAKE game :)
#  snake must move continuously, ---DONE
#  snake moves both ways, make only one
#  making code OOP would be nice practice
#  must make snake to move the moment game is launched or space/enter key hit to start game
#  initialize food once on map
#  once food is being eaten or impact made create food in new place
#  once food eaten extend snakes body
#  keep track of score on how many foods eaten
#  add difficulty levels
#  perhaps add snake animation or images ?
#  find better background ?
#  make game a bit more unique ?
#  game should be endless
#  perhaps instead of difficulty levels make game itself more difficult upon eating more and more foods
#  will FPS make game smoother ?

# width and snake_height of screen window
GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT = 700, 700
WIN = pygame.display.set_mode((GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT))
# title of window
pygame.display.set_caption("Snake")

# img for background of snake
GRASS = pygame.transform.scale(pygame.image.load(os.path.join(
    'C:\\Users\\Vartotojas\\Downloads\\images', 'grass00.png')), (GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT))

# x and y are coordinates on map where rectangle/snake head appears
x, y = 50, 50
# below are snakes heads/rectangles width and snake_height
snake_width, snake_height = 40, 40
# snake movement speed
velocity = 5


# randomly appearing food with diff coordinates every time
def random_food():
    return pygame.draw.circle(WIN, (0, 0, 0), (random.randint(0, 500), random.randint(0, 500)), 15.0)


# snakes/rectangles movement control will respond only to one of the keys pressed
# def snake_movement(keys):
#     global x, y
#     if keys[pygame.K_LEFT] and x > 0:
#         x -= velocity
#     elif keys[pygame.K_RIGHT] and x < GAME_WINDOW_WIDTH - width:
#         x += velocity
#     elif keys[pygame.K_UP] and y > 0:
#         y -= velocity
#     elif keys[pygame.K_DOWN] and y < GAME_WINDOW_HEIGHT - snake_height:
#         y += velocity

x_changed = 0
y_changed = 0
location = random.randint(0, 500), random.randint(0, 500)
black = (0, 0, 0)
radius = 15.0
blue = (0, 0, 255)


def main():
    global x, y, x_changed, y_changed, location

    running = True
    clock = pygame.time.Clock()
    while running:
        # for smoother game
        clock.tick(60)
        # loop through all evens within pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # if you click X or alt f4 game will close
                running = False
            if event.type == pygame.KEYDOWN:
                # initializing keys for pressing
                if event.key == pygame.K_LEFT:
                    x_changed = -velocity
                    y_changed = 0
                elif event.key == pygame.K_RIGHT:
                    x_changed = velocity
                    y_changed = 0
                elif event.key == pygame.K_UP:
                    y_changed = -velocity
                    x_changed = 0
                elif event.key == pygame.K_DOWN:
                    y_changed = velocity
                    x_changed = 0
        # boundaries designed so that if you touch them, game ends at the moment
        if x >= GAME_WINDOW_WIDTH - snake_width or x <= 0 or y >= GAME_WINDOW_HEIGHT - snake_height or y <= 0:
            running = False
        #  below reassigns new values to x and y
        x += x_changed
        y += y_changed
        # background added
        WIN.blit(GRASS, (0, 0))
        # todo FOOD MUST APPEAR in one spot until it is eaten and then appear in new place
        food = pygame.draw.circle(WIN, black, location, radius)
        # snakes head which will extend to body later
        head = pygame.draw.rect(WIN, blue, (x, y, snake_width, snake_height))
        # constantly updates screen
        pygame.display.update()
        # checks if snakes head has collided with food, if yes should create new food
        if food.colliderect(head):
            print("yum, test passed")
    pygame.quit()


# needed for launching code so that nothing else will be launched simultaneously as in example imports
if __name__ == "__main__":
    main()
