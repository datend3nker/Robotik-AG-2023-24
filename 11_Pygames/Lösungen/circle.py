# Speichert alle Kreise, die erstellt wurden
CIRCLES = []

class Circle:
    def __init__(self, pos:tuple[float, float], radius:float, color:tuple[int, int, int]):
        """
        Erstellt ein neues Circle-Objekt mit den angegebenen Parametern.

        Args:
            pos (tuple[float, float]): Die Position des Kreises als (x, y) Koordinaten.
            radius (float): Der Radius des Kreises.
            color (tuple[int, int, int]): Die Farbe des Kreises als RGB-Tupel.

        """
        self.pos = pos
        self.radius = radius
        self.color = color
        CIRCLES.append(self)

    def collides_with(self, other: 'Circle') -> bool:
        """
        Überprüft, ob dieser Kreis mit einem anderen Kreis kollidiert.

        Args:
            other (Circle): Der andere Kreis, mit dem die Kollision überprüft werden soll.

        Returns:
            bool: True, wenn eine Kollision vorliegt, False sonst.

        """
        distance_squared = (self.pos[0] - other.pos[0]) ** 2 + (self.pos[1] - other.pos[1]) ** 2
        radius_sum = self.radius + other.radius
        return distance_squared <= radius_sum ** 2
    
    def collides_with_other_circles(self) -> bool:
        """
        Überprüft, ob dieser Kreis mit anderen Kreisen in der CIRCLES-Liste kollidiert.

        Returns:
            bool: True, wenn eine Kollision mit einem anderen Kreis vorliegt, False sonst.

        """
        for circle in CIRCLES:
            if circle != self and self.collides_with(circle):
                return True
        return False

    def move(self, direct:tuple[float, float]) -> None:
        """
        Bewegt den Kreis um die angegebene Richtung, falls keine Kollision mit anderen Kreisen vorliegt.

        Args:
            direct (tuple[float, float]): Die Richtung, um die der Kreis bewegt werden soll, als (x, y) Koordinaten.

        """
        old_pos = self.pos
        self.pos = (self.pos[0] + direct[0], self.pos[1] + direct[1])
        if self.collides_with_other_circles():
            self.pos = old_pos