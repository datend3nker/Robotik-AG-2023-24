from Car import *

stuck = car(0, 0, "none", True)

print(stuck.is_alive)

print(stuck.pos_x, stuck.pos_y)

stuck.drive(20, 20, "north")

print(stuck.pos_x, stuck.pos_y)

stuck.speed(20)

