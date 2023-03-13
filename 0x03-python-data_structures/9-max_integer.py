#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        val = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > val:
                val = my_list[i]
            else:
                continue
            i += 1
    return val
