from src.usercalculations import UserCalculations
from src import app_ui as app
from src.reading import Reading
from rich.console import Console

console: Console = Console()
reading: Reading = Reading()

user: UserCalculations = None
while True:
    # Intro Screen
    app.start_app()
    quit = app.prompt_navigation()
    if quit:
        break

    while True:
        # Choose Number to calculate
        number_choice: str = app.prompt_reading_choice()
        app.clear_console()

        # Show description of chosen number reading
        description: dict = reading.get_description(number_choice)
        app.print_section(description)
        quit = app.prompt_navigation()
        if quit:
            break

        # Show Calculation directions for chosen number
        app.clear_console()
        directions = reading.get_directions(number_choice)
        app.print_section(directions)
        if number_choice != 'life_path':
            app.display_letter_table()

        quit = app.prompt_navigation()
        if quit:
            break

        # Gather additional user info if no info available
        if user is None:
            profile = app.setup_account()
            user_name = profile['username']
            birth_date = profile['birthday']
            user = UserCalculations(user_name, birth_date)

        # Display reading
        reading_num = user.get_reading_num(number_choice)
        individual_reading = reading.get_reading(reading_num)
        app.clear_console()
        app.print_section(individual_reading)

        quit = app.prompt_navigation()
        if quit:
            break
