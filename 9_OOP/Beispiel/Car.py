class car:
    def __init__(self, pos_x: int, pos_y: int, direction: str, is_alive: bool):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.direction = direction
        self.is_alive = is_alive
    
    def drive(self, pos_x: int, pos_y: int, direction: str):
        if self.is_alive:
            self.pos_x = pos_x
            self.pos_y = pos_y
            self.direction = direction
    
    def honk(self):
        print("mep mep")
    
    def explode(self):
        self.is_alive = False
    
    def speed(self, speed: int):
        print(f"I'm fast {speed}")

bmw = car(5, 5, "north", True)
bmw.honk()
