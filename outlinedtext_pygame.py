import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
font = pygame.font.SysFont(None, 64) # Use default system font

def draw_outlined_text(screen, text, font, text_color, outline_color, x, y, outline_thickness=2):
    # Render the outline text multiple times
    outline_surface = font.render(text, True, outline_color)
    
    # Blit the outline surface in different directions
    for dx in range(-outline_thickness, outline_thickness + 1):
        for dy in range(-outline_thickness, outline_thickness + 1):
            if dx != 0 or dy != 0:
                screen.blit(outline_surface, (x + dx, y + dy))
                
    # Render the main text on top
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, (x, y))

# Main loop example
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((30, 30, 30)) # Fill screen with a dark grey color
    
    # Example usage:
    draw_outlined_text(screen, "Hello World", font, (255, 255, 255), (255, 0, 0), 50, 50)
    
    pygame.display.flip()
    
pygame.quit()