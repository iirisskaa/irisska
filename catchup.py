from pygame import *
window = display.set_mode((700,500))
display.set_caption('Догонялки')
background = transform.scale(image.load('background.png'),(700,500))

k1 = 100
y1 = 300

k2 = 300
y2 = 300

sprite1 = transform.scale(image.load('sprite1.png'),(100,100))
sprite2 = transform.scale(image.load('sprite2.png'),(100,100))
speed = 10

run = True
clock = time.Clock()
FPS = 60

while run:
    window.blit(background,(0,0))
    window.blit(sprite1,( k1 ,y1))
    window.blit(sprite2,( k2,y2))

    for e in event.get():
        if e.type == QUIT:
            run = False

    keys_pressed = key.get_pressed()

    if keys_pressed[K_LEFT] and k1 > 5:
        k1 -= speed
    if keys_pressed[K_RIGHT] and k1 < 595:
        k1 += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 595:
        y1 += speed

    if keys_pressed[K_a] and k2 > 5:
        k2 -= speed
    if keys_pressed[K_d] and k2 < 595:
        k2 += speed
    if keys_pressed[K_w] and y2 > 5:
        y2 -= speed
    if keys_pressed[K_s] and y2 < 595:
        y2 += speed


    display.update()
    clock.tick(FPS)