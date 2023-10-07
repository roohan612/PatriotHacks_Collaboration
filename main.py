import pygame, sys

# initializes pygame
pygame.init() 


# window creation, attributes, and setup:
window : pygame.Surface             = pygame.display.set_mode()
WINDOW_SIZE : tuple[int, int]       = window.get_size()
ASPECT_RATIO : float                = window.get_width() / window.get_height()
WINDOW_TITLE : str                  = "Exploit"
FRAME_RATE : int                    = 60

pygame.display.set_caption(WINDOW_TITLE)


# clock
clock : pygame.time.Clock = pygame.time.Clock()


#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    window.fill((0, 0, 0)) 
    
    pygame.display.update()
    clock.tick(60)
    
