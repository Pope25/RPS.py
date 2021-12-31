# An Alarm Clock

import time

current_time = time.localtime()

hour = current_time.tm_hour
minute = current_time.tm_min
second = current_time.tm_sec

it_is_time_to_get_up = (hour>7) or (hour==7 and minute>29)

if it_is_time_to_get_up:
    print('IT IS TIME TO GET UP')
else:
    print('Go back to bed')
time.sleep(4)

print(' RISE AND SHINE')
time.sleep(4)

print(' THE EARLY BIRD GETS THE WORM')
time.sleep(4)

print('The time is', hour,':',minute,':',second)

time.sleep(15)
