def move(steps):
    steps_list = list(steps)
    iterator = 0
    for step in steps_list:
        if step == '(':
            iterator += 1
        if step == ')':
            iterator -= 1
    return iterator

def move_with_position(steps, breack_basement):
    steps_list = list(steps)
    iterator = 0
    position = 0
    for step in steps_list:
        position += 1
        if step == '(':
            iterator += 1
        if step == ')':
            iterator -= 1
        if iterator == breack_basement:
            break
    return {"move": iterator, "position": position}