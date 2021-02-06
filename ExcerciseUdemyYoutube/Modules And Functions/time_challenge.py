import pytz
import datetime

# choice = input("Hit enter to continue")
choice = 'lol'
list = ["Hawaii", 'Zulu']

# while choice != '0':
#     for city in list:
#         print(list.index(city) + 1, city)
#     time_zulu = pytz.timezone('Zulu')
#     time_hawaii = pytz.timezone('US/Hawaii')
#     local_times = datetime.datetime.now(time_zulu)
#     local_hawaii = datetime.datetime.now(time_hawaii)
#     if choice == "Hawaii".lower():
#         print("Hawaii local time is {}".format(local_hawaii))
#     if choice == 'Zulu':
#         print("Zulu local time is {}".format(local_times))
#     choice = input("Please choose your City from list: ")
#

while choice != '0':
    choice = input("Which zone you wanna check:")
    if choice == '0':
        break
    for zone in pytz.all_timezones:
        time_for_zone = pytz.timezone(zone)
        tz_display = datetime.datetime.now(time_for_zone)
        # print("{}".format(zone))
        if choice.lower() in zone.lower():
            print("-" * 100)
            print("{} date and time : \t\t{}".format(zone, tz_display))
            print("UTC time  \t\t\t\t\t\t\t\t\t{}".format(datetime.datetime.utcnow()))
            print("MY Local time is \t\t\t\t\t\t\t{}".format(datetime.datetime.now()))
            print("*" * 100)
            continue

# print("{}: {}".format(counter, zone))


# country = 'Europe/Vilnius'
# tz_display = pytz.timezone(country)
# local_time = datetime.datetime.now(tz=tz_display)
#
# print(local_time)
# print("UTC now is {}".format(datetime.datetime.utcnow()))
# print("-" * 100)

# for x in sorted(pytz.country_names):
#     print("{}: {}".format(x, pytz.country_names[x]), end=': ')
#     if x in pytz.country_timezones:
#         for zone in sorted(pytz.country_timezones[x]):
#             tz_display = pytz.timezone(zone)
#             local_time = datetime.datetime.now(tz=tz_display)
#             print("\t\t\t\t\t\t{}:  {}".format(zone, local_time))
#     else:
#         print("No time zone")

# input("Choose one of the 9 timezones below")

# while input != 0:
#     for zone in pytz.all_timezones:
#         print(zone)
#     break

# local_time = datetime.datetime.now()
# print(local_time)
# utc_time = datetime.datetime.utcnow()
# print(utc_time)
# print()
# aware_local = pytz.utc.localize(local_time).astimezone()
# print(aware_local, aware_local.tzinfo)
# aware_utc = pytz.utc.localize(utc_time)
# print(aware_utc, aware_utc.tzinfo)
#
# gap_time = datetime.datetime(2021, 1, 16, 17, 5, 0, 0)
# gap_time2 = datetime.datetime(2017, 12, 17, 20, 0, 0)
# result = gap_time - gap_time2
# print(result)
# print(gap_time)
# print(gap_time.timestamp())
# time_was = gap_time.timestamp()
# value_minutes = time_was / 60
# value_hours = value_minutes / 60
# value_days = value_hours / 24
# value_years = value_days / 365
#
# print(value_years)
