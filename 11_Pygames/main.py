import pygame
from circle import Circle

pygame.init()
speed = 100  # Pixel pro Sekunde

screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

running = True


# definiere hier deinen Kreis und ein Hindernis. Beide sind Circle-Objekte.
raise NotImplementedError("Definiere hier deinen Kreis und ein Hindernis. Beide sind Circle-Objekte.")


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
        raise NotImplementedError("Implementiere die Bewegung nach links")
    
    if pygame.K_RIGHT in keys_pressed:
        raise NotImplementedError("Implementiere die Bewegung nach rechts")
    
    if pygame.K_UP in keys_pressed:
        raise NotImplementedError("Implementiere die Bewegung nach oben")
    
    if pygame.K_DOWN in keys_pressed:
        raise NotImplementedError("Implementiere die Bewegung nach unten")

    

    screen.fill((255, 255, 255))
    # Render hier deine Kreise und Hindernis mithilfe von pygame.draw.circle()
    raise NotImplementedError("Render hier deine Kreise und Hindernis mithilfe von pygame.draw.circle()")

    pygame.display.flip()

pygame.quit()
