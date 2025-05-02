import pygame

# Player(x, y, width, height)
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 0, 0))  # Fill the player with red color
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.money = 0
        self.hp = 100
        self.skills = []
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Skill:
    def __init__(self, name, atk):
        self.name = name
        self.atk = atk
