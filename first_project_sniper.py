from pygame import *
from random import randint

window = display.set_mode((700, 500))
background = transform.scale(image.load('backg_sniper2.png'), (700, 500))
scope_frame = image.load('scope_3.png')

scope_frame.set_colorkey((255, 255, 255))

clock = time.Clock()
run = True

class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, width = 50, height = 50):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Gamesprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= 5
        if keys[K_d] and self.rect.x < 505:
            self.rect.x += 5
        if keys[K_s] and self.rect.y < 305:
            self.rect.y += 5
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= 5
    #def fire(self):
    #    bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 8, 15, 20)
    #    bullets.add(bullet)
    

scope = Player('scope.png', 0, 0, 3, 200, 200)
mask = Surface((700, 500), SRCALPHA)

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        #if e.type == KEYDOWN:
        #    if e.key == K_SPACE:
    window.blit(background, (0, 0))
    scope.move()
    scope.reset()
    mask.fill((0, 0, 0, 255))
    draw.circle(mask, (0, 0, 0, 0), scope.rect.center, 95)
    window.blit(mask, (0, 0))
    
    display.flip()
    clock.tick(60)
            