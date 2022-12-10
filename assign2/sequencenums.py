def sequenceUpTo(n):
    # create the default list
    default_list = [1, 2, 4]
    # create a new list
    newlist = []
    # check if number is -1
    if n == -1:
        return [-1]
    # check if number is 1
    elif n == 1:
        listvalue = default_list[0]
        newlist.append(listvalue)
        return newlist
    # check if number is 2
    elif n == 2:
        listvalue1 = default_list[0]
        listvalue2 = default_list[1]
        newlist.append(listvalue1)
        newlist.append(listvalue2)
        return newlist
    # check if number is 3
    elif n == 3:
        listvalue1 = default_list[0]
        listvalue2 = default_list[1]
        listvalue3 = default_list[2]
        newlist.append(listvalue1)
        newlist.append(listvalue2)
        newlist.append(listvalue3)
        return newlist
    # check if number is n the create the list
    else:
        newlist = newlist + default_list
        len_default = len(default_list)
        i = 1
        for i in range(1, n + 1):
            if i > len_default:
                next_value = newlist[-1] + newlist[-2] + newlist[-3]
                newlist.append(next_value)
        return newlist


# get the list and display
my_list = sequenceUpTo(5)
print(my_list)
