"""
This calls libraries that are needed. The pygame library is what the game is made with. The sys library is needed
to enable the close button to work in the window.
"""
# TODO create a main menu
import pygame
from sys import exit

'''
This begins the game. The font for the game is set. The window is created in the screen variable. The window name is 
made with set_caption and the games clock is created.
'''
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont("Comic Sans MS", 30)
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Dance Dance Revolution")
clock = pygame.time.Clock()
pygame.mixer.music.load("Roar Lion Roar.mp3", "mp3")
'''
This creates the main surface of the game; basically the game background.
'''
main_surface = pygame.Surface((1280, 720))
main_surface.fill((185, 217, 235))

# Create up arrow indicator
up_arrow_surface = pygame.image.load("arrow_indicator3.png").convert_alpha()
up_arrow_surface = pygame.transform.scale(up_arrow_surface, (112.33, 107.66))
up_arrow_surface_rect = up_arrow_surface.get_rect(topleft=(512, 10))

# Create down arrow indicator
down_arrow_surface = pygame.image.load("arrow_indicator3.png").convert_alpha()
down_arrow_surface = pygame.transform.scale(down_arrow_surface, (112.33, 107.66))
down_arrow_surface = pygame.transform.rotate(down_arrow_surface, 180)
down_arrow_surface_rect = down_arrow_surface.get_rect(topleft=(640, 10))

# create left arrow indicator
left_arrow_surface = pygame.image.load("arrow_indicator3.png").convert_alpha()
left_arrow_surface = pygame.transform.scale(down_arrow_surface, (112.33, 107.66))
left_arrow_surface = pygame.transform.rotate(down_arrow_surface, 270)
left_arrow_surface_rect = left_arrow_surface.get_rect(topleft=(384, 10))

# create right arrow indicator
right_arrow_surface = pygame.image.load("arrow_indicator3.png").convert_alpha()
right_arrow_surface = pygame.transform.scale(down_arrow_surface, (112.33, 107.66))
right_arrow_surface = pygame.transform.rotate(down_arrow_surface, 90)
right_arrow_surface_rect = right_arrow_surface.get_rect(topleft=(768, 10))

# create points surface
points_surface = my_font.render("Points: placeholder", False, (0, 0, 0))

'''
This class defines the arrow object which are the moving arrows on the screen. Each arrow has an x position, y position,
speed, and source image file. The class also defines to functions for arrows, 'spawn' which displays it on the screen,
and 'delete' which makes it a clear image on the screen.
'''


class Arrow(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, speed, source):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(source).convert_alpha()
        self.x = x_pos
        self.y = y_pos
        self.speed = speed
        self.rect = self.image.get_rect(topleft=(x_pos, y_pos))

    def spawn(self):
        self.image = pygame.transform.scale(self.image, (112.33, 107.66))
        screen.blit(self.image, self.rect)
        # print("spawned")

    def delete(self):
        self.image = pygame.image.load("clear_image.png")


start_time = pygame.time.get_ticks()
pygame.mixer.music.play()
# SONG. When what arrows should be spawned in ms. It takes 2366.66666... milliseconds to travel from bottom to arrow.
'''
Songs will be in a list form. It will be a list of tuples where the first element is the time the arrow should 
be spawned in milliseconds, the second element is its type, the third is the actual arrow object. The arrows travel
at the same speed so it is know how long it takes to reach the arrow indicator.
'''
#TODO create a real song.
test_song = [(1500, 'u', Arrow(512, 720, 5, "up_arrow.png")), (3000, 'd', Arrow(640, 720, 5, "down_arrow.png")),
             (5123, "l", Arrow(384, 720, 5, "left_arrow.png")), (6000, "r", Arrow(768, 720, 5, "right_arrow.png")),
             (6000, 'u', Arrow(512, 720, 5, "up_arrow.png"))]

'''
This while loop is the actual game. Each time it runs the game updates. 
'''
while True:
    '''
    This block enables the exit arrow in the window to work.
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    '''
    This creates the arrow indicator and point indicator surfaces that are static(unmoving).
    '''
    screen.blit(main_surface, (0, 0))
    screen.blit(up_arrow_surface, up_arrow_surface_rect)
    screen.blit(down_arrow_surface, down_arrow_surface_rect)
    screen.blit(left_arrow_surface, left_arrow_surface_rect)
    screen.blit(right_arrow_surface, right_arrow_surface_rect)
    screen.blit(points_surface, (1024, 10))

    ''''
    Main game logic. Each loop the elapsed time from the game start time is taken. A list called happening is created.
    It will contain all the arrows that are spawned and moving. We loop through the song and put the notes in the 
    happening list if we have reached the time it is supposed to spawn. The loop through the happening list updates
    all its contents' y coordinate;making it move. The last block of if statements check for collision using posiiton.
    '''
    elapsed_time = pygame.time.get_ticks() - start_time
    # print(elapsed_time)
    happening = []
    for note in test_song:
        if (note[0]) <= elapsed_time:
            if note[1] == 'u':
                note[2].spawn()
                happening.append(note)
            # UP_arrow.spawn()
            if note[1] == 'd':
                note[2].spawn()
                happening.append(note)
                # DOWN_arrow.spawn()
            if note[1] == 'l':
                note[2].spawn()
                happening.append(note)
            # LEFT_arrow.spawn()
            if note[1] == 'r':
                note[2].spawn()
                happening.append(note)
            # RIGHT_arrow.spawn()

    for note in happening:
        note[2].rect.y -= 5
        note[2].spawn()
    # print(happening)

    if happening:  # TODO button pressed are only working for up arrows after the first one. Must fix
        pressed = (pygame.key.get_pressed(), happening[-1][2].rect.y)
        if happening[-1][1] == 'u':
            if pressed[0][pygame.K_UP]:
                if 20 > (pressed[1] - 10) > -10:
                    happening[-1][2].delete()
                    print("Good!")
        if happening[-1][1] == 'd':
            if pressed[0][pygame.K_DOWN]:
                if 20 > (pressed[1] - 10) > -10:
                    happening[-1][2].delete()
                    print("Good!")
        if happening[-1][1] == 'l':
            if pressed[0][pygame.K_LEFT]:
                if 20 > (pressed[1] - 10) > -10:
                    happening[-1][2].delete()
                    print("Good!")
        if happening[-1][1] == 'r':
            if pressed[0][pygame.K_RIGHT]:
                if 20 > (pressed[1] - 10) > -10:
                    happening[-1][2].delete()
                    print("Good!")

    pygame.display.update()
    clock.tick(60)  # The while true loops should not run faster than 60 times per second
