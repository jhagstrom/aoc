import math
import numpy as np
from scipy.spatial.distance import cdist

def steps_between(start, goal):
    steps = 0
    stepper = start
    while (stepper[0] != goal[0] and stepper[1] != goal[1]):
        print(stepper)
        print(goal)
        x_dist = stepper[0] - goal[0]
        y_dist = stepper[1] - goal[1]
        print(x_dist)
        print(y_dist)
        x_dir = -1 if x_dist > 0 else 1
        y_dir = -1 if y_dist > 0 else 1
        print(x_dir)
        print(y_dir)
        if(abs(x_dist) > abs(y_dist)):
            n = stepper[0] + x_dir
            print(n)
            stepper = (n, stepper[1])
            steps += 1
        else:
            stepper = (stepper[0], stepper[1] + y_dir)
            steps += 1
    return steps 
        
        
def make_move(position, direction):
        return (position[0]+direction[0],position[1]+direction[1])

def valid_position(matrix, position):
    s = matrix.shape
    y = position[0]
    x = position[1]
    within_bounds =  -1 < y < s[0] and -1 < x < s[1]
    if(within_bounds):
        return matrix[position] == 0
    else:
        return False
left = (0, -1)
right = (0, 1)
up = (-1, 0)
down = (1, 0)

def move_next(matrix, direction, position):
    if(direction == up):
        try_left = make_move(position, left)
        if(valid_position(spiral_matrix,try_left)):
            position = try_left
            direction = left
        else:
            try_up = make_move(position, up)
            if(valid_position(spiral_matrix, try_up)):
                position = try_up
                direction = up
    elif(direction == left):
        try_down = make_move(position, down)
        if(valid_position(spiral_matrix,try_down)):
            position = try_down
            direction = down
        else:
            try_left = make_move(position, left)
            if(valid_position(spiral_matrix, try_left)):
                position = try_left
                direction = left
    elif(direction == down):
        try_right = make_move(position, right)
        if(valid_position(spiral_matrix,try_right)):
            position = try_right
            direction = right
        else:
            try_down = make_move(position, down)
            if(valid_position(spiral_matrix, try_down)):
                position = try_down
                direction = down
    elif(direction == right):
        try_up = make_move(position, up)
        if(valid_position(spiral_matrix,try_up)):
            position = try_up
            direction = up
        else:
            try_right = make_move(position, right)
            if(valid_position(spiral_matrix, try_right)):
                position = try_right
                direction = right
    return (position, direction)

seed = 23
horizontal_dim = math.ceil(math.sqrt(seed))
vertical_dim = math.ceil(math.sqrt(seed))
shape = (vertical_dim, horizontal_dim)
spiral_matrix = np.zeros(shape)
half_h_dim = horizontal_dim // 2
half_v_dim = vertical_dim // 2
middle = (half_v_dim, half_h_dim)
position = middle
spiral_matrix[position] = 1
number = 2
direction = right
position = make_move(position, direction)
last_position = position
while number < seed + 1:
    spiral_matrix[position] = number
    number += 1
    last_position = position
    next_step = move_next(spiral_matrix, direction, position)
    position = next_step[0]
    position = next_step[0]
    direction = next_step[1]
    
print(spiral_matrix)
print(last_position)
steps = steps_between(position, middle)
print('steps: ' + str(steps))



