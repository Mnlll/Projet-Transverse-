# Créer class bot : humains + voitures qui se baladent dans la ville
# 4 types de perso : homme( noir )  / femme ( asiatique ) / enfant (europeen ) / vieux (latino )
# Voitures
# contaminé : rougir
# non contaminé : blanc
# si virus touche bot ---> bot infecté ---> bot devient rouge
# si virus touche bot ---> +1 point
# si virus touche voiture ---> +5 points
####### OPTIONAL TASKS #######
# - vacciné : bleu
# animer les perso

import pygame


class Bot(pygame.sprite.Sprite):

    # Définition des caractéristiques des bot
    def __init__(self):
        super().__init__()
        # bot habillé en blanc au départ
        self.image = pygame.image.load('assets/tanjiro.png')
        self.rect = self.image.get_rect()
        self.life_max = 30
        self.life = 30
        self.velocity = 3
        self.rect.x = 1000
        self.rect.y = 350

    # Pour mettre les bots en mouvement


    def go_forward(self):
        self.rect.x -= self.velocity














########### A METTRE DANS LA CLASSE GAME ###########

# Appel de la classe Bot pour ajouter les bots au jeu
# from bot import Bot

    # dans le init
    # self.grp_bot = pygame.sprite.Group()
    # self.apparition_bot()

    # def apparition_bot(self):
        # bot = Bot()
        # self.grp_bot.add(bot)

# Lorsqu'un bot rencontre le virus
# si virus touche bot ---> bot infecté ---> bot devient rouge

    # def collision_virus(self,sprite,Group):
        # return pygame.sprite.spritecollide(sprite,group,False, pygame.sprite.collide_mask())




########## A METTRE DANS LE MAIN #############
# pour faire apparaître les bots sur l'ecran
# game.grp_bot.draw(fond)
