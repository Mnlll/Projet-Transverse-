import pygame
from game import Game


pygame.init()

# Generate window
pygame.display.set_caption('P L A G U E   D O D G E')
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
    game.start()
    # Show background

    # Check if game is running
    if game.is_running:
        # Run game
        game.update(window)
    # else:
        # Welcome window:
        
    # Refresh window
    pygame.display.flip()

    # Check events
    for event in pygame.event.get():
        # Close window
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    

    # Merge FPS with clock
    clock.tick(FPS)
