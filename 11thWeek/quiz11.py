#Problem A -- Sum values in range
def sum_range(start, stop):
    if start > stop:
        return 0
    else:
        return start + sum_range(start+1, stop)

#Problem B -- Duplicate Large Values
def duplicate_large(num_list):
    if num_list == []:
        return []
    elif num_list[0] >= 100:
        return 2*[num_list[0]] + duplicate_large(num_list[1:])
    else:
        return duplicate_large(num_list[1:])

#Problem C -- Only Digits
def get_digits(string):
    if string == '':
        return ''
    elif string[0].isdigit():
        return string[0] + get_digits(string[1:])
    else:
        return get_digits(string[1:])

def only_digits(string_list):
    if string_list == []:
        return []
    else:
        return [get_digits(string_list[0])] + only_digits(string_list[1:])
