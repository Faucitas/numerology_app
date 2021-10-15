from reading import Reading
from usercalculations import UserCalculations
from user import User
from art import tprint
import app_ui as app
from reading import Reading
from rich.console import Console

console = Console()
reading = Reading()

user = None
while True:
    # Intro Screen
    app.clear_console()
    app.display_heading()
    app.display_app_description()
    navigation = app.prompt_navigation()
    if navigation == "Quit":
        break

    while True:
        # Choose Number to calculate
        app.clear_console()
        app.display_heading()
        number_choice = app.prompt_reading_choice()

        # Show description of chosen Number
        print(number_choice)
        print(reading)
        description = reading.get_description(number_choice)

        app.clear_console()
        app.print_section(description)
        navigation = app.prompt_navigation()
        if navigation == "Quit":
            break

        # Show Calculations for chosen number
        app.clear_console()
        directions = reading.get_directions(number_choice)
        app.print_section(directions)
        if number_choice != 'life_path':
            app.display_letter_table()
        navigation = app.prompt_navigation()
        if navigation == 'Quit':
            break

        # Gather additional user info
        if user is None:
            app.clear_console()
            tprint("To calculate you unique numbers you'll need  to setup your profile first", font="thin3")
            user_name = app.prompt_user_name()
            birth_date = app.prompt_birth_date()
            user = UserCalculations(user_name, birth_date)

        # Display reading
        if number_choice == 'life_path':
            life_path = user.get_life_path_num()
            individual_reading = reading.get_reading(life_path)
        elif number_choice == 'soul_urge':
            soul_urge = user.get_soul_urge_num()
            individual_reading = reading.get_reading(soul_urge)
        elif number_choice == 'expression':
            expression = user.get_expression_num()
            individual_reading = reading.get_reading(expression)
        else:
            individual_reading = None
        app.clear_console()
        app.print_section(individual_reading)

        navigation = app.prompt_navigation()
        if navigation == 'Quit':
            break





