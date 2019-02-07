from hw1func import calculate_trip_length

liters_per_100km = float(input('Enter your fuel consumption in liters per 100km: '))
liters_in_tank = float(input('Enter quantity of fuel in tank: '))

print('trip length: ', calculate_trip_length(liters_per_100km, liters_in_tank))