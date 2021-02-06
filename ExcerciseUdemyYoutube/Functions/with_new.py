def reader():
    with open('C:\\Users\\37060\\Test.txt') as path:
        for line in path:
            if "world" in line.lower():
                print(line, end='')


cities2 = 'Palanga, Sventoji, Klaipeda, Vilnius'


def writer():
    with open('cities.txt', 'w') as city_file2:
        for city in cities2:
            print(city, file=city_file2)


writer()

# cities = []
# with open('cities.txt', 'r') as city_file:
#     for city in city_file:
#         cities.append(city.strip('\n'))

# print(cities)
# for city in cities:
#     print(city, end='')
