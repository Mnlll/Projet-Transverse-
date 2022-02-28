import pygame
pygame.init()

#Creation classe player qui représente le virus dans le jeu

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 10
        self.max_health = 10
        self.attack = 1
        self.velocity = 20
        self.image = pygame.image.load('assets/virus.png')
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 50
        self.origin_image = self.image
        self.angle = 0
        self.player = pygame.sprite.Group()

    def rotate(self):
        #tourner le virus
        self.angle += 10
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move_high(self):
        self.rect.y += self.velocity

    def move_down(self):
        self.rect.y -= self.velocity * 1.25

#generer notre joueur


#Charger notre player

# player = Player

#Déplacement du joueur



#appliquer l'image de mon joueur



#verifier si le joueur souhaite aller en haut ou non


#Gestion des dégâts du joueur


def damage(self, amount):
    #Infliger les dégâts au gens
    self.health -= amount