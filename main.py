from reading import Reading
from usercalculations import UserCalculations
from user import User
from art import tprint
from rich.console import Console
console = Console()




fn = "thomas"
md = "edward"
ln = "smith"
bd = "02011982"

tommy = UserCalculations(fn, md, ln, bd)


expression = tommy.get_life_path_num()



# Get and print a reading
reading = Reading(expression).get_description()
print_reading(reading)