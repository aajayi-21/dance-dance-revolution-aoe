import pygame
from sys import exit

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont("Comic Sans MS", 30)
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Dance Dance Revolution")
clock = pygame.time.Clock()


main_surface = pygame.Surface((1280,720))
main_surface.fill((185, 217, 235))

# Create up arrow indicator
up_arrow_surface = pygame.image.load("arrow_indicator3.png").convert_alpha()
up_arrow_surface = pygame.transform.scale(up_arrow_surface,(112.33,107.66))
up_arrow_surface_rect = up_arrow_surface.get_rect(topleft = (512,10))

#Create down arrow indicator
down_arrow_surface = pygame.image.load("arrow_indicator3.png").convert_alpha()
down_arrow_surface = pygame.transform.scale(down_arrow_surface,(112.33,107.66))
down_arrow_surface = pygame.transform.rotate(down_arrow_surface, 180)
down_arrow_surface_rect = down_arrow_surface.get_rect(topleft = (640,10))

#create left arrow indicator
left_arrow_surface = pygame.image.load("arrow_indicator3.png").convert_alpha()
left_arrow_surface = pygame.transform.scale(down_arrow_surface,(112.33,107.66))
left_arrow_surface = pygame.transform.rotate(down_arrow_surface, 270)
left_arrow_surface_rect = left_arrow_surface.get_rect(topleft = (384,10))

#create right arrow indicator
right_arrow_surface = pygame.image.load("arrow_indicator3.png").convert_alpha()
right_arrow_surface = pygame.transform.scale(down_arrow_surface,(112.33,107.66))
right_arrow_surface = pygame.transform.rotate(down_arrow_surface, 90)
right_arrow_surface_rect = right_arrow_surface.get_rect(topleft = (768,10) )

#create points surface
points_surface = my_font.render("Points: placeholder", False, (0,0,0))


''' PROBABLY DELETE
#create up arrow
up_arrow = pygame.image.load("up_arrow.png").convert_alpha()
up_arrow = pygame.transform.scale(up_arrow, (112.33, 107.66))
up_arrow_y = 720
up_arrow_rect = up_arrow.get_rect(topleft=(512,720))
#up_arrow = pygame.Rect
'''


class Arrow(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos,speed,source):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(source).convert_alpha()
        self.x = x_pos
        self.y = y_pos
        self.speed = speed
        self.rect = self.image.get_rect(topleft = (x_pos,y_pos))

    def spawn(self):
        self.image = pygame.transform.scale(self.image, (112.33, 107.66))
        screen.blit(self.image,self.rect)
        #print("spawned")

start_time = pygame.time.get_ticks()

#CREATE ARROWS
UP_arrow = Arrow(512,720,5,"up_arrow.png")

#SONG. When what arrows should be spawned
test_song = [(1000,'u')]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(main_surface,(0,0))
    screen.blit(up_arrow_surface,up_arrow_surface_rect)
    screen.blit(down_arrow_surface,down_arrow_surface_rect)
    screen.blit(left_arrow_surface,left_arrow_surface_rect)
    screen.blit(right_arrow_surface,right_arrow_surface_rect)
    screen.blit(points_surface,(1024,10))
  #  screen.blit(up_arrow,up_arrow_rect)

    #Game Logic
    elapsed_time = pygame.time.get_ticks() - start_time
    print(elapsed_time)
    happening = []
    for note in test_song:
        if (note[0]) <= elapsed_time:
            if note[1] == 'u':
                happening.append(UP_arrow)
                UP_arrow.spawn()



    pressed = (pygame.key.get_pressed(), elapsed_time)

    for note in happening:
        note.rect.y -= note.speed
        note.spawn()

    '''
    if up_arrow_rect.collidepoint(512,10) or pressed[0][pygame.K_w]:
        print(pressed[1])
        up_arrow.fill((0,0,0))
'''


    pygame.display.update()
    clock.tick(60) #The while true loops should not run faster than 60 times per second








