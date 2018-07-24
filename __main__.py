import sys
from os import path
from lib import day_one

basepath = path.dirname(__file__)

def run_project(args):
    print('Run: ------- Day 1 -------')
    filepath = path.abspath(path.join(basepath,"lib/puzzel/day_one.txt"))
    steps = "()"
    with open(filepath, "r") as file:
        for line in file:
            steps = line.strip()
    print("move = ", day_one.move(steps))
    print("move untill -1 = ", day_one.move_with_position(steps, -1))

if __name__ == '__main__':
    run_project(sys.argv)