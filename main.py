from reading import Reading

readings = Reading()
numbers = [1, 2, 4, 5, 6, 7, 8, 9, 11, 22]
for number in numbers:
    num_as_str = str(number)
    readings.get_reading('soul_urge', num_as_str)
    readings.print_reading()
