import pygame
from game import Game


pygame.init()

# Generate window
pygame.display.set_caption('Name')
window = pygame.display.set_mode((1400 , 720))

# import backgrounds


# Frames Per Second
clock = pygame.time.Clock()
FPS = 60

# Load game
game = Game()

# Show window
run = True
while run :
    # Show background

    # Check if game is running
    if game.is_running:
        # Run game
        game.update(window)
    # else:
        # Welcome window:

    # Check events
    for event in pygame.event.get():
        # Close window
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    # Refresh window
    pygame.display.flip()

    # Merge FPS with clock
    clock.tick(FPS)