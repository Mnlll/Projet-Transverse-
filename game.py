import pygame
from bot import Man
from bot import Woman
from bot import OldWoman
from bot import OldMan
from bot import OldManSick
from player import Player

import time


# Game class
class Game:
    # Default settings
    def __init__(self):
        # Game off
        self.is_running = False
        # Generate player
        # Generate obstacles
        # Generate NPC
        self.grp_bots = pygame.sprite.Group()
        # Generate sound
        # Initialize score
        self.score = 0
        self.font = pygame.font.SysFont('Courrier', 50)
        # Catch events
        self.pressed = {}
        self.player = Player()
        for i in range(5):
            self.apparition_bot(Man)
            self.apparition_bot(Woman)
            self.apparition_bot(OldWoman)
            self.apparition_bot(OldMan)

    # Start game
    def start(self):
        self.is_running = True
        #self.apparition_bot(Man)
        #self.apparition_bot(Woman)

        # Show obstacles
        # Show NPC
        # game.grp_bots.draw(background)

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
        self.grp_bots.draw(window)
        # Apply obstacles animation

        # Apply obstacles NPC
        #for bot in self.grp_bots:
            #bot.go_forward()

        # Check fly
        # if self.pressed.get(pygame.K_SPACE): # Mettre condition pour que le player ne sorte pas de la fenetre
            # self.player.fly()
        # else:
            # Player tombe avec gravité

    # Collision with entity
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    # Spawn entity
    def apparition_bot(self, bot_class_name):
        self.grp_bots.add(bot_class_name.__call__(self))
        



