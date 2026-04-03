from pygame import *
from random import randint

window = display.set_mode((700, 500))
background = transform.scale(image.load('backg_sniper2.png'), (700, 500))
scope_frame = image.load('scope_3.png')
scope_frame.set_colorkey((255, 255, 255))

mixer.init()
shoot = mixer.Sound('shoot2.mp3')
reload_sound = mixer.Sound('reload.mp3')
shoot.set_volume(0.1)

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

        


class Enemy(Gamesprite):
    def __init__(self, player_image, x, y, speed, width = 50, height = 50):
        super().__init__(player_image, x, y, speed, width, height)
        self.start = x
        self.direction = 'right'
        
    def update(self):
        if self.rect.x <= self.start - 50:
            self.direction = 'right'
        if self.rect.x > self.start + 50:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


        

enemys = sprite.Group()
for i in range(2):
    enemy = Enemy('enemy3.png', randint(150, 550), randint(150, 350), randint(1, 3), 20, 30)
    enemys.add(enemy)

scope = Player('scope.png', 0, 0, 3, 200, 200)
mask = Surface((700, 500), SRCALPHA)

ammo = 10
reload_time = 2000
reload = False
reload_start = 0
font.init()


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE and reload == False:
                if ammo > 0:
                    shoot.play()
                    ammo -= 1
                    for enemy in enemys:
                        if enemy.rect.collidepoint(scope.rect.center):
                            enemys.remove(enemy)
                            enemy = Enemy('enemy3.png', randint(150, 550), randint(150, 350), randint(1, 3), 20, 30)
                            enemys.add(enemy)
                if ammo == 0:
                    reload = True
                    reload_sound.play()
                    reload_start = time.get_ticks()
    if reload == True:
        now = time.get_ticks()
        if now - reload_start >= reload_time:
            ammo = 10
            reload = False 

    window.blit(background, (0, 0))
    scope.move()
    scope.reset()
    enemys.draw(window)
    enemys.update()
    mask.fill((0, 0, 0, 255))
    draw.circle(mask, (0, 0, 0, 0), scope.rect.center, 95)
    window.blit(mask, (0, 0))
    ammo_text = font.SysFont('Arial', 30).render('Ammo: ' + str(ammo) + '/10', True, (255, 255, 255))
    window.blit(ammo_text, (525, 450))
    display.flip()
    clock.tick(60)
            