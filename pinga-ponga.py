from pygame import *

windows = display.set_mode((700, 500))
display.set_caption('пугаме виндоу')
game = True
final = False
count = 0
clock = time.Clock()
background = transform.scale(image.load("i (4).jpg"), (700, 500))


class rectangle(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed

    def reset(self):
        windows.blit(self.image, (self.rect.x, self.rect.y))

class player(rectangle):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 345: 
            self.rect.y += self.speed
        
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 345: 
            self.rect.y += self.speed

leftrok = player('left.png', 625, 150, 5, 70, 150)
rightrok = player('right.png', 0, 150, 5, 70, 150)



while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    windows.blit(background, (0, 0))

    if final != True:
        leftrok.reset()
        leftrok.update_left()
        rightrok.reset()
        rightrok.update_right()

        

    display.update()
    clock.tick(60)


























































