def check_elements(elements, itype):
    result = False
    for x in elements:
        if type(x) ==  itype:
            result = True
        else:
            result = False
            break
    return result


def exclusive_datatype_list(lst, datatype):
    boolean = True
    i = 0
    while boolean and i < len(lst):
        if type(lst[i]) != datatype:
            boolean = False
        i+=1
    return boolean

def check_min(dig1, dig2):
    if dig1 < dig2:
        return dig1
    else:
        return dig2


def find_min(elements):
    if check_elements(elements, int) == True and len(elements) > 0:
        if len(elements) == 1:
            return elements[0]
        else:
            return check_min(elements[0], find_min(elements[1:]))
    else:
        return -1


def make_sum(dig1, dig2):
    return dig1+dig2


def sum_all(elements):
    if check_elements(elements, int) == True and len(elements) > 0:
        if len(elements) == 1:
            return elements[0]
        else:
            return make_sum(elements[0], sum_all(elements[1:]))
    else:
        return -1


def find_possible_strings(character_set, n):
    """TODO: complete for Step 3"""
    if check_elements(character_set, str):
        if n == 1:
            return character_set
        empty_set = []
        for x in character_set:
            temp_set = find_possible_strings(character_set, n-1)
            for z in temp_set:
                empty_set.append(x+z)
    else:
        return []    
    return empty_set


if __name__ == "__main__":
    my_list = [5,6,8,9,3,11]
    my_list2 = [1,2,3,4,5]
    myset = ['y', 'x']
    print(find_possible_strings(myset, 3))
    print(find_min(my_list))
    print(sum_all(my_list2))


