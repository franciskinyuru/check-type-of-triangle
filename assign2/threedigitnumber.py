import math


def checkRatio():
    for i in range(100, 333):
        value1 = i
        value2 = i * 2
        value3 = i * 3
        gcd1 = math.gcd(math.gcd(value1, value2), value3)
        # print(str(value1 // gcd1) + ":" + str(value2 // gcd1) + ":" + str(value3 // gcd1))
        print(str(value1) + " " + str(value2) + " " + str(value3) + "")


checkRatio()
