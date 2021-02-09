cities = ['NewYork', 'Moscow', 'Leningrad', 'new dehli', 'Toronto']
print(cities)
print(len(cities))

print(cities[0])
print(cities[-1])
print(cities[3].title())

cities[3] = 'Tula'
print(cities)

cities.append('Kursk')
print(cities)

cities.insert(4, 'Feodosiya')
print(cities)

del cities[-1]
print(cities)

cities.remove('Moscow')
print(cities)

deleted_city = cities.pop()  # Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент

print("Deleted city is: " + deleted_city)
print(cities)

cities.reverse()
print(cities)

