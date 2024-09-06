import pygame
from pygame import Vector2
from math import floor

dimensions = [50, 50]

size = [10, 10]

def generate_color(dimensions):
    return_list = [0 for _ in range(int(dimensions[0] * dimensions[1]))]
    return(return_list)

color = generate_color(dimensions)

pygame.init()
W, H=500, 500
screen = pygame.display.set_mode([W, H])
pygame.display.set_caption("Game Thing")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial" , 12 , bold = True)

running = True


def fps_counter():
    fps = str(int(clock.get_fps()))
    fps_t = font.render(fps , 1, pygame.Color("RED"))
    screen.blit(fps_t,(0,0))

def playerinput(color, size, dimensions):
    global event, previous_cursor_pos, painted, mode, previous_keys
    current_keys=pygame.key.get_pressed()
    mousekey=pygame.mouse.get_pressed()
    mousepos=pygame.mouse.get_pos()
    
    
    if not previous_keys[pygame.K_SPACE] and current_keys[pygame.K_SPACE]:
        mode = (mode + 1) % 3
        print(mode)

    if not previous_keys[pygame.K_RETURN] and current_keys[pygame.K_RETURN]:
        print()
        print(color)
        print()

    cursor_pos = [round((mousepos[0] - size[0] / 2) / size[0]), round((mousepos[1] - size[1] / 2) / size[1])]

    if not(previous_cursor_pos == cursor_pos):
        painted = False
        
    if painted == False and pygame.mouse.get_pressed()[0]:
        painted = True
        cursor_index = (cursor_pos[1] * dimensions[0]) + cursor_pos[0]
        if cursor_index < 0:
            cursor_index = 0
        elif cursor_index > len(color) - 1:
            cursor_index = len(color) - 1

        if mode == 0:
            if color[cursor_index] == 0:
                color[cursor_index] = 1
            else:
                color[cursor_index] = 0
        elif mode == 1:
            color[cursor_index] = 1
        else: 
            color[cursor_index] = 0
    
    previous_cursor_pos = cursor_pos
    previous_keys = current_keys
        

class World:
    def __init__(self):
        pass
    
    def show(self, color, size, dimensions):
        screen.fill((100, 100, 100))
        for item_index in range(len(color)):
            self.drawrect = pygame.Rect(0, 0, size[0], size[1])
            self.drawrect.x = size[0] * (item_index % dimensions[0])
            self.drawrect.y = size[1] * floor(item_index / dimensions[0])
            if color[item_index] == 1:
                item_color = (255, 255, 255)
            else:
                item_color = (0, 0, 0)
            pygame.draw.rect(screen, item_color, self.drawrect)

previous_keys = pygame.key.get_pressed()
mode = 0
previous_cursor_pos = []
painted = False

w=World()
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    playerinput(color, size, dimensions)
    w.show(color, size, dimensions)
    
    fps_counter()
    pygame.display.update()

pygame.quit()