"""
Leetcode 1041: Robot Bounded In Circle
On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

Example:
Input: "GGLLGG"
Output: true
Explanation:
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
"""


def isRobotBounded(instructions):

    directions = {
        'yl' : '-x',  # x and y are axis, l and r are directions
        '-yl' : 'x',
        'xl' : 'y',
        '-xl' : '-y',
        'yr' : 'x',
        '-yr':'-x',
        'xr' : '-y',
        '-xr' : 'y'
    }
    current_dir = 'y'
    state = (0,0)
    for dir in instructions:
        if dir == 'G':
            if current_dir == 'y':
                state = (state[0],state[1]+1)
            if current_dir == '-y':
                state = (state[0],state[1]-1)
            if current_dir == 'x':
                state = (state[0]+1,state[1])
            if current_dir == '-x':
                state = (state[0]-1,state[1])
        if dir == 'L':
            current_dir = directions[current_dir + 'l']
        if dir == 'R':
            current_dir = directions[current_dir + 'r']
    if state == (0,0):
        return True
    else:
        if current_dir != 'y':
            return True
    return False

##instructions = 'GGLLGG'
instructions = 'GG'
print(isRobotBounded(instructions))
