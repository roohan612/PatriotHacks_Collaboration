import pygame, sys, time

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


# timer
current_time : float = 0.0
delta_time : float = 0.0


# player
player_hitbox : pygame.Rect = pygame.Rect(0, 0, 32, 64)
player_velocity : pygame.Vector2 = pygame.Vector2(0.0, 0.0)
player_moved : pygame.Vector2 = pygame.Vector2(0, 0)

#game loop
current_time = time.time()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player_moved.x = 1
            if event.key == pygame.K_a:
                player_moved.x = -1
            if event.key == pygame.K_SPACE:
                player_moved.y = -1 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player_moved.x = 0
            if event.key == pygame.K_a:
                player_moved.x = 0
        
        
    new_time : float = time.time()
    delta_time = new_time - current_time
    current_time = new_time        


    if player_moved.x != 0:
        player_velocity.x += 16 * delta_time * player_moved.x
    else:
        player_velocity.x *= delta_time
    player_hitbox.x += player_velocity.x
    
    
    draw_surface.fill((0, 0, 0)) 
    pygame.draw.rect(draw_surface, (255, 0, 0), player_hitbox, 1)

    
    pygame.transform.scale(draw_surface, WINDOW_SIZE, window)
    pygame.display.update()
    clock.tick(60)
    
