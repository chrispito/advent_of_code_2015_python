def lights_count(string, xx):
    puzzel = get_puzzel(xx)

    return lights_count_p(string, puzzel)

def lights_count_p(string, puzzel):
    new_string = ""
    action = None
    if 'turn on' in string:
        new_string = string.replace('turn on', '').strip()
        action = 1
    if 'toggle' in string:
        new_string = string.replace('toggle', '').strip()
        action = 2
    if 'turn off' in string:
        new_string = string.replace('turn off', '').strip()
        action = 3
    
    coord = get_coordinate(new_string)
    sub_puzzel = get_sup_puzzel(coord['x'], coord['y'])
    puzzel = set_light_status(puzzel, sub_puzzel, action)
    return puzzel

def get_coordinate(string):
    data = string.split('through')
    x = data[0].strip().split(',')
    y = data[1].strip().split(',')

    return {'x': tuple(list(map(int, x))), 'y': tuple(list(map(int, y)))}

def get_puzzel(xx):
    puzzel = {}
    for i in range(0, xx):
        for j in range(0, xx):
            index = str(i) + ',' + str(j)
            puzzel[index] =  (i, j, 0, 0)
    return puzzel

def get_sup_puzzel(xx, yy):
    min_x = min(xx[0], yy[0])
    max_x = max(xx[0], yy[0])
    min_y = min(xx[1], yy[1])
    max_y = max(xx[1], yy[1])
    puzzel = set()
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            index = str(i) + ',' + str(j)
            puzzel.add(index)
    return puzzel

def set_light_status(puzzel, sub_puzzel, action):
    for key in sub_puzzel:
        value = puzzel[key]
        if action == 1:
            puzzel[key] = (value[0], value[1], 1, value[3] + 1) 
        if action == 2:
            puzzel[key] = (value[0], value[1], 1 if value[2] == 0 else 0, value[3] + 2) 
        if action == 3:
            b = value[3] - 1
            puzzel[key] = (value[0], value[1], 0, 0 if b < 0 else b)
    return puzzel

def count_lighted(puzzel):
    count = 0
    for key, value in puzzel.items():
        if value[2] == 1:
            count += 1
    return count

def count_brightness(puzzel):
    count = 0
    for key, value in puzzel.items():
        count += value[3]
    return count


# https://plot.ly/python/dot-plots/