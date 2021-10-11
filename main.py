from reading import Reading
from calculations import Calculations
from user import User

fn = "thomas"
md = "edward"
ln = "Smith"
bd = "02011982"

tommy = User(fn, md, ln, bd)

calculations = Calculations(tommy)
expression = calculations.get_expression_num()
print(expression)


# Get and print a reading
reading = Reading()
reading.get_reading('expression', str(expression))
reading.print_reading()

