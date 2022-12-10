from datetime import datetime, timedelta
from datetime import date

def time2Midnight():
    today = date.today()
    tomorrow = today + timedelta(1)
    midnight = datetime.combine(tomorrow, datetime.min.time())
    custom_time = input("Enter time \n")
    custom_time_array = custom_time.split(":")
    if custom_time_array[0] == "00" and custom_time_array[1] == "00" and custom_time_array[2] =="00":
        print("0:0:0")
    else:
        time_object = datetime.strptime(custom_time, '%H:%M:%S').time()
        my_custom_time = datetime.combine(today, time_object)

        time_diff = midnight-my_custom_time
        custom_time_diff = str(time_diff).split(":")
        if custom_time_diff[1] == "00":
            custom_time_diff[1] = "0"
        elif custom_time_diff[1][0] == '0':
            custom_time_diff[1] = custom_time_diff[1][1]
        else:
            custom_time_diff[1] = custom_time_diff[1]

        if custom_time_diff[2] == "00":
            custom_time_diff[2] = "0"
        elif custom_time_diff[2][0] == '0':
            custom_time_diff[2] = custom_time_diff[2][1]
        else:
            custom_time_diff[2] = custom_time_diff[2]

        new_time = custom_time_diff[0] + ":" + custom_time_diff[1] + ":" + custom_time_diff[2]

        print(new_time)


time2Midnight()

