from pygame import *

windows = display.set_mode((700, 500))
display.set_caption('пугаме виндоу')
game = True
final = False
count = 0
clock = time.Clock()
background = transform.scale(image.load("i (4).jpg"), (700, 500))


while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    windows.blit(background, (0, 0))

    if final != True:
        pass

    display.update()
    clock.tick(60)


























































