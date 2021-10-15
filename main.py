from reading import Reading
from usercalculations import UserCalculations
from user import User
from art import tprint
import app_ui as app
from rich.console import Console
console = Console()



while True:
    app.clear_console()
    app.display_heading()
    app.display_app_description()
    navigation = app.prompt_navigation()

    if navigation == "Quit":
        break

    app.clear_console()
    app.display_heading()
    user_name = app.prompt_user_name()
    app.greet_user(user_name)
