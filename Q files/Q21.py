# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point.
# If the distance is a float, then just print the nearest integer.

import math
position = [0,0]
while True:
    movement = input('Enter movement (UP/DOWN/LEFT/RIGHT) and number of steps: ')
    if not movement:
        break
    direction = movement.split()[0]
    steps = movement.split()[1]
    if direction == 'UP':
        position[0] += int(steps)
    elif direction == 'DOWN':
        position[0] -= int(steps)
    elif direction == 'LEFT':
        position[1] -= int(steps)
    elif direction == 'RIGHT':
        position[1] += int(steps)
    else:
        pass
distance = round(math.sqrt(position[0]**2 + position[1]**2))
print('The distance from starting point is:', distance)
