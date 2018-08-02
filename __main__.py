import sys
from os import path
from lib import day_1, day_2, day_3, day_4, day_5, day_6, day_7
import plotly
import plotly.graph_objs as go

basepath = path.dirname(__file__)

def plot_data(puzzel):
    x_axis = []
    y_axis = []
    for key, value in puzzel.items():
        if value[2] == 1:
            x_axis.append(value[0])
            y_axis.append(value[1])

    trace1 = {"x": x_axis, 
        "y": y_axis, 
        "marker": {"color": "pink", "size": 2}, 
        "mode": "markers", 
        "name": "Women", 
        "type": "scatter"
    }

    data = [trace1]
    layout = {"title": "Gender Earnings Disparity", 
            "xaxis": {"title": "Annual Salary (in thousands)", }, 
            "yaxis": {"title": "School"}}
    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename='basic_dot-plot.png')

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

    print('Run: ------- Day 5 -------')
    filepath = path.abspath(path.join(basepath,"lib/puzzel/day_5.txt"))
    with open(filepath, "r") as file:
        nice_string_count = 0
        nice_string_count_new = 0
        for line in file:
            if day_5.nice_string_check(line):
                nice_string_count += 1
            if day_5.nice_string_check_new(line):
                nice_string_count_new += 1
        
    print("total nice string = ", nice_string_count)
    print("total nice string [New] = ", nice_string_count_new)

    # print('Run: ------- Day 6 -------')
    # filepath = path.abspath(path.join(basepath,"lib/puzzel/day_6.txt"))
    # lights_count = 0
    # brightness_count = 0
    # with open(filepath, "r") as file:
    #     puzzel = day_6.get_puzzel(1000)
    #     for line in file:
    #         puzzel = day_6.lights_count_p(line, puzzel)

    #     lights_count  = day_6.count_lighted(puzzel)
    #     brightness_count  = day_6.count_brightness(puzzel)
    #     # plot_data(puzzel)

    # print("total lights = ", lights_count)
    # print("total brightness = ", brightness_count)

    print('Run: ------- Day 7 -------')
    filepath = path.abspath(path.join(basepath,"lib/puzzel/day_7.txt"))
    data = []
    with open(filepath, "r") as file:
        for line in file:
            data.append(line.strip())
    print(len(data))
    dictionary = day_7.binary_operator(data)

    print("value of a = ", dictionary["a"])


if __name__ == '__main__':
    run_project(sys.argv)