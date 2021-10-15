from usercalculations import UserCalculations
from art import tprint
import app_ui as app
from reading import Reading
from rich.console import Console

console: Console = Console()
reading: Reading = Reading()

user: UserCalculations = None
while True:
    # Intro Screen
    app.clear_console()
    app.display_heading()
    app.display_app_description()
    quit = app.prompt_navigation()
    if quit:
        break

    while True:
        # Choose Number to calculate
        app.clear_console()
        app.display_heading()
        number_choice: str = app.prompt_reading_choice()

        # Show description of chosen Number
        description: dict = reading.get_description(number_choice)
        app.clear_console()
        app.print_section(description)

        quit = app.prompt_navigation()
        if quit:
            break

        # Show Calculations for chosen number
        app.clear_console()
        directions = reading.get_directions(number_choice)
        app.print_section(directions)
        if number_choice != 'life_path':
            app.display_letter_table()
        quit = app.prompt_navigation()
        if quit:
            break

        # Gather additional user info
        if user is None:
            app.clear_console()
            tprint("To calculate you unique numbers you'll need  to setup your profile first", font="thin3")
            user_name = app.prompt_user_name()
            birth_date = app.prompt_birth_date()
            user = UserCalculations(user_name, birth_date)


        # Display reading
        reading_num = user.get_reading_num(number_choice)
        individual_reading = reading.get_reading(reading_num)
        app.clear_console()
        app.print_section(individual_reading)

        quit = app.prompt_navigation()
        if quit:
            break
