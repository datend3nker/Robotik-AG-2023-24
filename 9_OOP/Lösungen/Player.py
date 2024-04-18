import Position

class Player:
    def __init__(self, name: str, player_class: str, damage: int, position: Position, lp: int):
        """
        Initializes a Player object.

        Args:
            name (str): The name of the player.
            player_class (str): The class of the player.
            damage (int): The damage inflicted by the player.
            position (Position): The position of the player.
            lp (int): The life points of the player.
        """
        self.name = name
        self.player_class = player_class
        self.damage = damage
        self.position = position
        self.lp = lp

    def get_damage(self, damage: int):
        """
        Decreases the player's life points by the specified amount of damage.

        Args:
            damage (int): The amount of damage to be inflicted on the player.
        """
        self.lp -= damage

    def move(self, new_position: Position):
        """
        Moves the player to the specified position.

        Args:
            new_position (Position): The new position of the player.
        """
        self.position = new_position