def timeSingUp(special_digit):
    series = [*range(1, special_digit + 1)]
    return series


# loop to get the series of numbers
def rangeofnumbers(start, special_num):
    orig_list = [*range(start, 10000, 1)]
    new_list = []
    for i in orig_list:
        if str(special_num) in str(i):
            new_list = [*range(start, i + 1)]
            break
    return new_list


# get the special number from in put
def specialNum():
    special_list = [3, 4, 5, 6, 7, 8]
    special_digit = input("Enter special digit \n")
    special_digit = int(special_digit)
    if special_digit in special_list:
        return special_digit
    else:
        return "invalid special number"


# get the series upto first 4 digit number
def checkLast():
    my_final_list = []
    special = specialNum()
    series = timeSingUp(special)
    my_final_list = my_final_list + series
    new_start = series[-1] * special
    new_series = rangeofnumbers(new_start, special)
    my_final_list = my_final_list + new_series
    new_start = new_series[-1] * special

    for i in range(1, 100):
        if len(str(new_start)) < 4:
            new_start = new_series[-1] * special
            new_series = rangeofnumbers(new_start, special)
            my_final_list = my_final_list + new_series

    filtered_list = []
    less_list = []
    for i in my_final_list:
        if len(str(i)) == 4:
            filtered_list.append(i)
        else:
            less_list.append(i)
    final_list = []
    firstvalue = filtered_list[0]
    less_list.append(firstvalue)
    return less_list


myseries = checkLast()
# display the series
print(', '.join(str(e) for e in myseries))
