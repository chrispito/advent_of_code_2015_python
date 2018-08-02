import numpy

def binary_operator(data):
    dictionary = {}
    old_data = []
    while len(data) > 0:
        if old_data == data:
            print("Same data")
            print(dictionary)
            print(data)
            break
        old_data = data.copy()
        for string in data:
            string_list = string.split(' ')
            if "NOT" in string:
                if string_list[1] in dictionary:
                    dictionary[string_list[3]] = ~dictionary[string_list[1]]
                    data.remove(string)

            elif "AND"in string:
                if RepresentsInt(string_list[0]) and string_list[2] in dictionary:
                    dictionary[string_list[4]] = int(string_list[0]) & dictionary[string_list[2]]
                    data.remove(string)
                if RepresentsInt(string_list[2]) and string_list[0] in dictionary:
                    dictionary[string_list[4]] = dictionary[string_list[20]] & int(string_list[2])
                    data.remove(string)
                if RepresentsInt(string_list[0]) and RepresentsInt(string_list[2]):
                    dictionary[string_list[4]] = int(string_list[0]) & int(string_list[2])
                    data.remove(string)
                if string_list[0] in dictionary and string_list[2] in dictionary:
                    dictionary[string_list[4]] = dictionary[string_list[0]] & dictionary[string_list[2]]
                    data.remove(string)
                
            elif "OR" in string:
                if string_list[0] in dictionary and string_list[2] in dictionary:
                    dictionary[string_list[4]] = dictionary[string_list[0]] | dictionary[string_list[2]]
                    data.remove(string)
                
            elif "LSHIFT" in string:
                if string_list[0] in dictionary:
                    dictionary[string_list[4]] = dictionary[string_list[0]] << int(string_list[2])
                    data.remove(string)
                
            elif "RSHIFT" in string:
                if string_list[0] in dictionary:
                    dictionary[string_list[4]] = dictionary[string_list[0]] >> int(string_list[2])
                    data.remove(string)
                
            elif "->" in string:
                if RepresentsInt(string_list[0]):
                    dictionary[string_list[2]] = numpy.uint16(int(string_list[0]))
                    data.remove(string)
                elif string_list[0] in dictionary:
                    dictionary[string_list[2]] = dictionary[string_list[0]]
                    data.remove(string)
            else:
                pass

    return dictionary


def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False