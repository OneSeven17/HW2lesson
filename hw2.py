from hw2func import calculate_roll_quantity

room_length = float(input('Enter your room length in cm: '))
room_width = float(input('Enter your room width in cm: '))
room_height = float(input('Enter your room height in cm: '))
roll_width = float(input('Enter roll width in cm: '))
roll_length = float(input('Enter roll length in cm: '))

print('roll quantity:', calculate_roll_quantity (room_length, room_width, room_height, roll_width, roll_length))

