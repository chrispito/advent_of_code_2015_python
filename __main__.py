import sys
from os import path
from lib import day_1, day_2, day_3, day_4

basepath = path.dirname(__file__)

def run_project(args):
    print('Run: ------- Day 1 -------')
    filepath = path.abspath(path.join(basepath,"lib/puzzel/day_1.txt"))
    steps = ""
    with open(filepath, "r") as file:
        for line in file:
            steps = line.strip()
    print("move = ", day_1.move(steps))
    print("move untill -1 = ", day_1.move_with_position(steps, -1))

    print('Run: ------- Day 2 -------')
    filepath = path.abspath(path.join(basepath,"lib/puzzel/day_2.txt"))
    with open(filepath, "r") as file:
        surface = 0
        feet_of_ribbon = 0
        for line in file:
            surface += day_2.surface(line)
            feet_of_ribbon += day_2.feet_of_ribbon(line)
    print("total surface = ", surface)
    print("total feet_of_ribbon = ", feet_of_ribbon)

    print('Run: ------- Day 3 -------')
    filepath = path.abspath(path.join(basepath,"lib/puzzel/day_3.txt"))
    with open(filepath, "r") as file:
        min_home_count = 0
        min_home_count_2 = 0
        for line in file:
            min_home_count += day_3.min_home_count(line)
            min_home_count_2 += day_3.min_home_count_2(line)
    print("total house = ", min_home_count)
    print("total min_home_count_2 = ", min_home_count_2)

    print('Run: ------- Day 4 -------')
    result = day_4.hash_check("bgvyzdsv")
    print("md5 [5] Zeros = ", result)
    result = day_4.hash_check_2("bgvyzdsv")
    print("md5 [6] Zeros = ", result)

if __name__ == '__main__':
    run_project(sys.argv)