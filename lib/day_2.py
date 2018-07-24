def surface(data):
    data_str = data.split('x')
    data_int = [int(val) for val in data_str]
    l = data_int[0]
    w = data_int[1]
    h = data_int[2]

    data_int.remove(max(data_int))
    small_1 = data_int[0]
    small_2 = data_int[1]
    
    return 2 * (l*w + w*h + l*h) + (small_1 * small_2)

def feet_of_ribbon(data):
    data_str = data.split('x')
    data_int = [int(val) for val in data_str]
    l = data_int[0]
    w = data_int[1]
    h = data_int[2]

    data_int.remove(max(data_int))
    small_1 = data_int[0]
    small_2 = data_int[1]
    
    return (l * w * h) + 2 * (small_1 + small_2)