import questionary as qy
from art import text2art, tprint
from rich.console import Console
from rich.table import Table
import json
import os

console = Console()

with open('data/app_data.json', 'r') as file:
    data: dict = json.load(file)
LETTERS_TABLE: dict = data['letters_table']
APP_DESCRIPTION: dict = data['app_description']


def prompt_user_name() -> object:
    validation = lambda text: True if text.isalpha() else "Please enter only letters"
    console.print("Please enter your full birth name", style="bold color(3)", )
    console.print("As it appears on your birth certificate", style="italic")
    user: object = qy.form(
        first_name=qy.text("First name", validate=validation),
        middle_name=qy.text("Middle name", validate=validation),
        last_name=qy.text("Last name", validate=validation)
    ).ask()
    return user


def prompt_birth_date() -> object:
    validation = lambda text: True if text.isdigit() else "Please enter the a number"
    year_validation = lambda text: True if len(text) == 4 else "Enter 4 digit year"
    birth_date: object = qy.form(
        birth_month=qy.text("Month of birth", validate=validation),
        birth_day=qy.text("Day of birth", validate=validation),
        birth_year=qy.text("Year of birth", validate=year_validation)
    ).ask()
    return birth_date


def prompt_reading_choice() -> str:
    reading_choice: str = qy.select(
        "Which number would you like to calculate",
        choices=[
            "Life Path Number",
            "Soul Urge Number",
            "Expression Number"
        ]
    ).ask()
    if reading_choice == "Life Path Number":
        reading_choice = "life_path"
    elif reading_choice == "Soul Urge Number":
        reading_choice = "soul_urge"
    elif reading_choice == "Expression Number":
        reading_choice = "expression"
    return reading_choice


def prompt_navigation() -> bool:
    nav_choice: str = qy.select(
        "Would you like to continue?",
        choices=[
            "Continue",
            "Quit"
        ]
    ).ask()
    return True if nav_choice == 'Quit' else False


def print_section(section: dict) -> None:
    heading: str = section['heading']
    title: str = section['title']
    body: str = section['body_paragraphs']
    tprint(heading, font="thin3")
    print("")
    console.print(title, style="bold")
    print("")
    for paragraph in body:
        console.print(paragraph)
        print("")


def display_heading() -> None:
    heading_text: str = "Numerologoy"
    heading: str = text2art(heading_text.upper(), font="cybermedium")
    print(heading)


def display_letter_table() -> None:
    title: str = "Numerology alphabet conversion chart"
    table: Table = Table(title=title)
    # Create table headers
    for number in LETTERS_TABLE:
        table.add_column(number, justify="center", style="cyan", no_wrap=True)
    # Fill table rows
    for i in range(0, 3):
        table.add_row(
            LETTERS_TABLE['1'][i],
            LETTERS_TABLE['2'][i],
            LETTERS_TABLE['3'][i],
            LETTERS_TABLE['4'][i],
            LETTERS_TABLE['5'][i],
            LETTERS_TABLE['6'][i],
            LETTERS_TABLE['7'][i],
            LETTERS_TABLE['8'][i],
            LETTERS_TABLE['9'][i]
        )
    # Print table
    console.print(table)


def display_app_description() -> None:
    heading: str = APP_DESCRIPTION['heading']
    description = {
        'heading': "Calculate your unique numbers",
        'title': APP_DESCRIPTION['heading'],
        'body_paragraphs': APP_DESCRIPTION['paragraphs']
    }

    print_section(description)


def clear_console() -> None:
    command: str = 'clear'
    # If Machine is running on Windows, use cls
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
