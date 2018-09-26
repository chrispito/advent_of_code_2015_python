import re
from copy import deepcopy

def string_count(string):
    (raw_string, to_remove) = code(string)
    code_count = len(string)
    str_len = len(string) - to_remove
    return (str_len, code_count)

def string_encode_count(string):
    code_count = len(string)
    (raw_string, to_add) = encode(string)
    encode_count = len(string) + to_add
    return (encode_count, code_count)

def code(text):
    expr = re.finditer(r"(\\[\\\"])|(\\(x[a-f0-9]{2}))", text)
    expr_length = len(list(expr))
    expr = re.finditer(r"(\\[\\\"])|(\\(x[a-f0-9]{2}))", text)
    if (expr_length != 0):
        count_1 = 0
        count_2 = 0
        for match in expr:
            g1 = match.group(1)
            g2 = match.group(2)
            if (g1 != None):
                count_1 += len(g1) - 1
            if (g2 != None):
                count_2 += len(g2) - 1
        return (text, count_1 + count_2 + 2)
    else:
        return (text, 2)

def encode(text):
    expr = re.finditer(r"(\\[\\\"])|(\\(x[a-f0-9]{2}))", text)
    expr_length = len(list(expr))
    expr = re.finditer(r"(\\[\\\"])|(\\(x[a-f0-9]{2}))", text)
    if (expr_length != 0):
        count_1 = 0
        count_2 = 0
        for match in expr:
            g1 = match.group(1)
            g2 = match.group(2)
            if (g1 != None):
                count_1 += 2
            if (g2 != None):
                count_2 += 1
        return (text, count_1 + count_2 + 4)
    else:
        return (text, 4)