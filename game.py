import pygame

from bot import Bot

# Game class
class Game:
    # Default settings
    def __init__(self):
        # Game off
        self.is_running = False
        # Generate player
        # Generate obstacles
        # Generate NPC
        # Generate sound
        # Initialize score
        self.score = 0
        self.font = pygame.font.SysFont('Courrier', 50)
        # Group of bots
        self.grp_bots = pygame.sprite.Group()
        # Catch events
        self.pressed = {}
        self.apparition_bot()

    # Start game
    def start(self):
        self.is_running = True
        # Show obstacles
        # Show NPC

    # Game over
    def game_over(self):
        self.is_running = False
        # Reset game
        self.score = 0
        # Sound

    # Score
    def add_score(self, points = 1):
        self.score += points

    # Update window
    def update(self, window):
        # Show score
        score_text = self.font.render(f'Score : {self.score}', 1, (0, 0, 0))
        window.blit(score_text, (20, 20))

        # Show player

        # Refresh player animation

        # Keep obstacles

        # Keep NPC

        # Apply obstacles animation

        # Apply obstacles NPC

        # Check fly
        # if self.pressed.get(pygame.K_SPACE): # Mettre condition pour que le player ne sorte pas de la fenetre
            # self.player.fly()
        #else:
            # Player tombe avec gravité

    # Collision with entity
    #def check_collision(self, sprite, group):
        #return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    # Spawn entity
    def apparition_bot(self):
        bot = Bot()
        self.grp_bots.add(bot)
