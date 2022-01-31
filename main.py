import pygame
from game import Game


pygame.init()

# Generate window
pygame.display.set_caption('P L A G U E   D O D G E')
window = pygame.display.set_mode((1400 , 720))

# import backgrounds
background = pygame.image.load('assets/background.png')

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
    else:
        # Welcome window:
        window.blit(background, (0, 0))
        pygame.display.flip()

    # Check events
    for event in pygame.event.get():
        # Close window
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    # Refresh window
    # pygame.display.flip()

    # Merge FPS with clock
    clock.tick(FPS)

    # Spawn bots on the screen
    game.grp_bots.draw(background)

    # To get the bots back
    for bot in game.grp_bots:
        bot.go_forward()




