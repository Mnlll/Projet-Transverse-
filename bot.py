import random

import pygame


class Bot(pygame.sprite.Sprite):

    # Définition des caractéristiques des bot
    def __init__(self, game, name):
        super().__init__()
        self.game = game
        self.image = pygame.image.load(f'assets/{name}.png')
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 5)
        self.rect.x = random.randint(1700, 2400)
        self.rect.y = 500

    # Pour mettre les bots en mouvement

    def go_forward(self):
        self.rect.x -= self.velocity


# Create class for the man
class Man(Bot):

    # ne fonctionne pas
    def __init__(self, game):
        super().__init__(game, 'man')
        #while game.start:
            #if self.game.check_collision(game.player, game.grp_bots):
                #super().__init__('man_sick', game)
                #print("OKKKK")


# Create class for the sick man
class SickMan(Bot):

    def __init__(self, game):
        super().__init__(game, 'man_sick')


# Create class for the woman
class Woman(Bot):

    def __init__(self, game):
        super().__init__(game, 'woman')


# Create class for the sick woman
class SickWoman(Bot):

    def __init__(self, game):
        super().__init__(game, 'woman_sick')


# Create class for the old man
class OldMan(Bot):

    def __init__(self, game):
        super().__init__(game, 'old_man')


# Create class for the old man sick
class OldManSick(Bot):

    def __init__(self, game):
        super().__init__(game, 'old_man_sick')


# Create class for the old woman
class OldWoman(Bot):

    def __init__(self, game):
        super().__init__(game, 'old_woman')


# Create class for the old woman sick
class OldWomanSick(Bot):

    def __init__(self, game):
        super().__init__(game, 'old_woman_sick')

