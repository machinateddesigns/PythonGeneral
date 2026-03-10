
import pygame

# Initialization
pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# Rectangles
trigger_rect = pygame.Rect(50, 50, 100, 50)
moving_rect = pygame.Rect(50, 200, 50, 50)
is_animating = False
velocity = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if trigger_rect.collidepoint(event.pos):
                is_animating = True # Start animation

    # Animation Logic
    if is_animating:
        moving_rect.x += velocity
        if moving_rect.x > 600: # Reset if out of bounds
            moving_rect.x = 0
            is_animating = False

    # Drawing
    screen.fill((30, 30, 30)) # Clear screen
    pygame.draw.rect(screen, (255, 0, 0), trigger_rect) # Red trigger
    pygame.draw.rect(screen, (0, 255, 0), moving_rect) # Green moving rect
    
    pygame.display.flip()
    clock.tick(60) # 60 FPS

pygame.quit()