## `Circle`-Klasse erstellen
### Aufgabenstellung: Erstellen einer `Circle` Klasse

In dieser Aufgabe werdet ihr eine Klasse `Circle` erstellen, die Kreise repräsentiert und verschiedene Methoden implementiert, um mit diesen Kreisen zu arbeiten. Befolgt die untenstehenden Schritte sorgfältig und überprüft eure Arbeit regelmäßig.

#### Aufgabe 1: Klasse `Circle` erstellen

1. Erstelle eine leere Liste `CIRCLES`, die alle erstellten Kreise speichern soll.
    ```python
    CIRCLES = []
    ```

2. Definiere die Klasse `Circle` mit einem Initialisierungsmethoden `__init__`.
    - Die `__init__` Methode soll die Parameter `pos` (Position als Tupel von (x, y)), `radius` (Radius des Kreises), und `color` (Farbe als RGB-Tupel) annehmen.
    - Setze die übergebenen Werte auf die Instanzvariablen `self.pos`, `self.radius`, und `self.color`.
    - Füge die erstellte Instanz der `CIRCLES` Liste hinzu.
    ```python
    class Circle:
        def __init__(self, pos: tuple[float, float], radius: float, color: tuple[int, int, int]):
            self.pos = pos
            self.radius = radius
            self.color = color
            CIRCLES.append(self)
    ```

#### Aufgabe 2: Kollision zwischen zwei Kreisen überprüfen

3. Implementiere die Methode `collides_with`, die überprüft, ob dieser Kreis mit einem anderen Kreis kollidiert.
    - Berechne den Abstand zwischen den Mittelpunkten der beiden Kreise.
    - Vergleiche diesen Abstand mit der Summe der Radien der beiden Kreise.
    - Wenn der Abstand kleiner oder gleich der Summe der Radien ist, kollidieren die Kreise.

#### Aufgabe 3: Kollision mit anderen Kreisen in der Liste überprüfen

4. Implementiere die Methode `collides_with_other_circles`, die überprüft, ob dieser Kreis mit einem anderen Kreis in der `CIRCLES`-Liste kollidiert.
    - Iteriere durch die `CIRCLES`-Liste.
    - Überprüfe für jeden Kreis (außer sich selbst) mit der Methode `collides_with`, ob eine Kollision vorliegt.
    - Gib `True` zurück, wenn eine Kollision gefunden wurde, sonst `False`.

#### Aufgabe 4: Kreis bewegen

5. Implementiere die Methode `move`, die den Kreis um eine angegebene Richtung verschiebt, sofern keine Kollision mit anderen Kreisen vorliegt.
    - Nimm die Parameter `direct` (Richtung als Tupel von (x, y)).
    - Aktualisiere die Position des Kreises basierend auf der angegebenen Richtung.
    - Überprüfe mit `collides_with_other_circles`, ob eine Kollision vorliegt.
    - Wenn eine Kollision vorliegt, setze die Position zurück auf die alte Position.


### Beispiel zur Orientierung

Hier ist ein Beispiel, wie ihr eure Klasse testen könnt, nachdem ihr sie implementiert habt:
```python
# Erstellen von zwei Kreisen
circle1 = Circle((0, 0), 5, (255, 0, 0))
circle2 = Circle((10, 0), 5, (0, 255, 0))

# Überprüfen, ob sie kollidieren
print(circle1.collides_with(circle2))  # Sollte False ausgeben

# Bewegen eines Kreises und Überprüfung der Kollision
circle2.move((-5, 0))
print(circle1.collides_with(circle2))  # Sollte True ausgeben
```

### Testen mit pytest

Eure Implementierung wird mit pytest getestet, um die Korrektheit sicherzustellen.

## Kreise in Pygames rendern
### Aufgabenstellung: Integrieren der `Circle` Klasse in ein Pygame Projekt

In dieser Aufgabe werdet ihr Schritt für Schritt die vorhandenen `NotImplementedError`-Stellen in der `main.py` entfernen und durch Code ersetzen, der eure zuvor erstellte `Circle` Klasse nutzt. Ihr werdet einen Kreis bewegen und dessen Kollision mit einem Hindernis überprüfen.

#### Aufgabe 1: Initialisierung der Kreise

1. Entfernt den `NotImplementedError` und definiert zwei `Circle` Objekte:
    - Einen Kreis, der vom Benutzer gesteuert wird.
    - Ein Hindernis.
    - Setzt die Position, den Radius und die Farbe für beide Kreise.

#### Aufgabe 2: Kreisbewegung implementieren

2. Entfernt die `NotImplementedError` in den Bereichen für die Bewegungssteuerung des Kreises.
    - Implementiert die Bewegung nach links, rechts, oben und unten basierend auf den Tastatureingaben.
    - Nutzt die `move` Methode eurer `Circle` Klasse, um den Kreis zu bewegen.
    - Die Bewegung erfolgt in Pixeln pro Sekunde, multipliziert mit der vergangenen Zeit (`dt`), um die Bewegungsgeschwindigkeit zu kontrollieren.
    - Stellt sicher, dass der Kreis nur dann bewegt wird, wenn keine Kollision mit einem anderen Kreis vorliegt.

#### Aufgabe 3: Rendern der Kreise

3. Entfernt den `NotImplementedError` im Render-Abschnitt.
    - Nutzt `pygame.draw.circle`, um den Kreis und das Hindernis zu zeichnen.
    - Zeichnet die Kreise basierend auf deren Position und Farbe.

### Hinweise zur Implementierung

#### Initialisierung der Kreise

- Erstellt zwei Instanzen der `Circle` Klasse: einen für den Spieler und einen als Hindernis.
- Beispiel: Überlegt euch, wie ihr Position, Radius und Farbe für die Kreise sinnvoll wählen könnt.

#### Kreisbewegung

- Nutzt die Tastatureingaben (Pygame-Events `KEYDOWN` und `KEYUP`), um die Bewegungsrichtung festzulegen.
- Überlegt euch, wie ihr die Position des Kreises basierend auf der Richtung und der vergangenen Zeit (`dt`) aktualisieren könnt.
- Nutzt die `move` Methode eurer `Circle` Klasse, um die Bewegung zu implementieren.
- Stellt sicher, dass der Kreis sich nur bewegt, wenn keine Kollision mit anderen Kreisen vorliegt.

#### Rendern der Kreise

- Verwendet `pygame.draw.circle`, um die Kreise auf dem Bildschirm zu zeichnen.
- Überlegt euch, wie ihr die Positionen und Farben der Kreise an `pygame.draw.circle` übergeben könnt.
- Aktualisiert den Bildschirm, um die gezeichneten Kreise anzuzeigen.
