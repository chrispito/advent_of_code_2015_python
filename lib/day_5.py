import re

def nice_string_check(string):
    return (check_first_condition(string) and
    check_second_condition(string) and check_third_condition(string))

def check_first_condition(string):
    count = 0
    for char in ['a', 'e', 'i', 'o', 'u']:
        count += string.count(char) 
    return True if count >= 3 else False

def check_second_condition(string):
    single = set(list(string))
    result = False
    for char in single:
        if (char + char) in string:
            result = True
            break
    return result
            
def check_third_condition(string):
    result = True
    for char in ['ab', 'cd', 'pq', 'xy']:
        if char in string:
            result = False
            break
    return result

def nice_string_check_new(string):
    return (check_first_condition_new(string) and check_second_condition_new(string))

def check_first_condition_new(string):
    match = re.search(r"([a-z][a-z]).*\1", string)
    return True if match else False


def check_second_condition_new(string):
    match = re.search(r"([a-z])[a-z]\1", string)
    return True if match else False