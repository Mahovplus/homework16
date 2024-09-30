def get_multiplied_digits(number):
    str_number = str(int(number))
    first = int(str_number[0])
    if 1 < len(str_number):
        return first * get_multiplied_digits(int(str_number[1:]))
    elif 1 > len(str_number):
        return 1
    else:
         return first






result = get_multiplied_digits(40203)
print(result)
