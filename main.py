import pygame, sys

# initializes pygame
pygame.init() 


# window creation, attributes, and setup:
window : pygame.Surface             = pygame.display.set_mode()
draw_surface : pygame.Surface       = pygame.Surface((16 * 16, 16 * 9))
WINDOW_SIZE : tuple[int, int]       = window.get_size()
ASPECT_RATIO : float                = window.get_width() / window.get_height()
WINDOW_TITLE : str                  = "Exploit"
FRAME_RATE : int                    = 60

pygame.display.set_caption(WINDOW_TITLE)


# clock
clock : pygame.time.Clock = pygame.time.Clock()


# player
player_hitbox : pygame.Rect = pygame.Rect(0, 0, 32, 64)


#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    
    window.fill((0, 0, 0)) 
    pygame.draw.rect(draw_surface, (255, 0, 0), player_hitbox, 1)

    
    pygame.transform.scale(draw_surface, WINDOW_SIZE, window)
    pygame.display.update()
    clock.tick(60)
    
