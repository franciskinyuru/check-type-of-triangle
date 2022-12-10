# start to sing up
def timeSingUp(special_digit):
    series = [*range(1, special_digit + 1)]
    return series


# get the series numbers
def rangeofnumbers(start, special_num):
    orig_list = [*range(start, 10000, 1)]
    new_list = []
    for i in orig_list:
        if str(special_num) in str(i):
            new_list = [*range(start, i + 1)]
            break
    return new_list


# get the series of number upto 4 nums count while passing special num
def checkLast(special):
    my_final_list = []
    special = special
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


# get the longest series as a tuple
def longest():
    list_len = {}
    myseries2 = checkLast(2)
    list_len['2'] = len(myseries2)
    myseries3 = checkLast(3)
    list_len['3'] = len(myseries3)
    myseries4 = checkLast(4)
    list_len['4'] = len(myseries4)
    myseries5 = checkLast(5)
    list_len['5'] = len(myseries5)
    myseries6 = checkLast(6)
    list_len['6'] = len(myseries6)
    myseries7 = checkLast(7)
    list_len['7'] = len(myseries7)
    myseries8 = checkLast(8)
    list_len['8'] = len(myseries8)
    myseries9 = checkLast(9)
    list_len['9'] = len(myseries9)
    longest_sequence = max(list_len.items(), key=lambda k: k[1])
    tolist = list(longest_sequence)
    tolist[0] = int(tolist[0])
    totuple = tuple(tolist)
    print(totuple)


longest()
