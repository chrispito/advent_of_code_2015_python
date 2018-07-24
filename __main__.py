import sys
from os import path
from lib import day_one, day_two

basepath = path.dirname(__file__)

def run_project(args):
    print('Run: ------- Day 1 -------')
    filepath = path.abspath(path.join(basepath,"lib/puzzel/day_one.txt"))
    steps = ""
    with open(filepath, "r") as file:
        for line in file:
            steps = line.strip()
    print("move = ", day_one.move(steps))
    print("move untill -1 = ", day_one.move_with_position(steps, -1))

    print('Run: ------- Day 2 -------')
    filepath = path.abspath(path.join(basepath,"lib/puzzel/day_two.txt"))
    with open(filepath, "r") as file:
        surface = 0
        feet_of_ribbon = 0
        for line in file:
            surface += day_two.surface(line)
            feet_of_ribbon += day_two.feet_of_ribbon(line)
    print("total surface = ", surface)
    print("total feet_of_ribbon = ", feet_of_ribbon)

if __name__ == '__main__':
    run_project(sys.argv)