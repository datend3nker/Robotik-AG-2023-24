import pygame
from circle import Circle

pygame.init()
speed = 100  # Pixel pro Sekunde

screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

running = True

circle = Circle(pos=(250, 250), radius=75, color=(0, 0, 255))
obstacle = Circle(pos=(100, 100), radius=25, color=(255, 0, 0))

keys_pressed = set()  # Speichert die aktuell gedrückten Tasten

while running:

    dt = clock.tick(60) / 1000.0  # Zeit seit dem letzten Frame in Sekunden

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Überprüfe Tastendruck-Ereignisse
        if event.type == pygame.KEYDOWN:
            keys_pressed.add(event.key)

        # Überprüfe Tastenloslass-Ereignisse
        if event.type == pygame.KEYUP:
            keys_pressed.discard(event.key)

    # Berechne die neue Position des Kreises basierend auf den gedrückten Tasten und der vergangenen Zeit
    if pygame.K_LEFT in keys_pressed:
        circle.move((-speed * dt, 0))
    if pygame.K_RIGHT in keys_pressed:
        circle.move((speed * dt, 0))
    if pygame.K_UP in keys_pressed:
        circle.move((0, -speed * dt))
    if pygame.K_DOWN in keys_pressed:
        circle.move((0, speed * dt))

    

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, circle.color, circle.pos, circle.radius)
    pygame.draw.circle(screen, obstacle.color, obstacle.pos, obstacle.radius)

    pygame.display.flip()

pygame.quit()
