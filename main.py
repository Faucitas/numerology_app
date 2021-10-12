from reading import Reading
from usercalculations import UserCalculations
from user import User

fn = "thomas"
md = "edward"
ln = "smith"
bd = "02011982"

tommy = UserCalculations(fn, md, ln, bd)


expression = tommy.get_expression_num()



# Get and print a reading
reading = Reading()
reading.get_reading(expression)
reading.print_reading()

