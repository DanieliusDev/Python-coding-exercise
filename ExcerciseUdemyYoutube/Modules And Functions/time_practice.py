import time
from time import perf_counter


def first_clock():
    return time.time()


print(first_clock())


def second_clock():
    return perf_counter()


print(second_clock())


def third_clock():
    print(time.get_clock_info("monotonic"))
    return time.monotonic()


print(third_clock())


def fourth_time():
    return time.process_time()


print(fourth_time())

print(time.get_clock_info("monotonic"))
# print(time.get_clock_info("clock"))
print(time.get_clock_info("perf_counter"))
print(time.get_clock_info("process_time"))
print(time.get_clock_info("time"))
