import hashlib

def hash_check(data):
    result = "aa"
    iteration = 0
    while  not result.startswith('00000'):
        new_data = data + str(iteration)
        h = hashlib.md5(new_data.encode('utf8'))
        iteration += 1
        result = h.hexdigest()

    return iteration - 1

def hash_check_2(data):
    result = "aa"
    iteration = 0
    while  not result.startswith('000000'):
        new_data = data + str(iteration)
        h = hashlib.md5(new_data.encode('utf8'))
        iteration += 1
        result = h.hexdigest()

    return iteration - 1

