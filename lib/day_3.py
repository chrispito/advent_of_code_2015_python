def min_home_count(data):
    steps = list(data)
    start = (0, 0)
    homes = {start}
    current = start
    for step in steps:
        current_x = current[0]
        current_y = current[1]
        if step == '>':
            current_x += 1
        elif step == '<':
            current_x -= 1
        elif step == '^':
            current_y += 1
        elif step == 'v':
            current_y -= 1
        current = (current_x, current_y)
        homes.add(current)

    return len(homes)

def min_home_count_2(data):
    steps = list(data)
    start = (0, 0)
    homes = {start}
    current_1 = start
    current_2 = start
    current = current_1
    turn = False
    for step in steps:
        current_x = current[0]
        current_y = current[1]
        if step == '>':
            current_x += 1
        elif step == '<':
            current_x -= 1
        elif step == '^':
            current_y += 1
        elif step == 'v':
            current_y -= 1

        if turn:
            current = current_1
            current_2  = (current_x, current_y)
        else:
            current = current_2
            current_1  = (current_x, current_y)
        
        homes.add((current_x, current_y))
        turn = not turn

    return len(homes)
