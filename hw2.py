room_length = float(input('Enter your room length in cm: '))
room_width = float(input('Enter your room width in cm: '))
room_height = float(input('Enter your room height in cm: '))
roll_width = float(input('Enter roll width in cm: '))
roll_length = float(input('Enter roll length in cm: '))

perimeter = room_length * 2 + room_width * 2
strip_quantity = round(perimeter / roll_width + 0.5) #the result will not be true, if the result of the division is an integer
strip_quantity_in_roll = roll_length / (room_height + 10)
roll_quantity = round(strip_quantity / strip_quantity_in_roll + 0.5) #the result will not be true, if the result of the division is an integer

print(strip_quantity) #left to check
print(strip_quantity_in_roll) #left to check
print('roll quantity:', roll_quantity)

