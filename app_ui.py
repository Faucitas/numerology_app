import questionary as qy
from art import text2art, tprint
from rich.console import Console
from rich.table import Table
import json
import os

console = Console()

with open('data/letters.json', 'r') as file:
    data = json.load(file)
LETTERS_TABLE = data['letters_table']
APP_DESCRIPTION = data['app_description']


def prompt_user_name():
    validation = lambda text: True if text.isalpha() else "Please enter only letters"
    console.print("Please enter your full birth name", style="bold color(3)", )
    console.print("As it appears on your birth certificate", style="italic")
    user: object = qy.form(
        first_name=qy.text("First name", validate=validation),
        middle_name=qy.text("Middle name", validate=validation),
        last_name=qy.text("Last name", validate=validation)
    ).ask()
    return user


def prompt_birth_date():
    validation = lambda text: True if text.isdigit() else "Please enter the a number"
    year_validation = lambda text: True if len(text) == 4 else "Enter 4 digit year"
    birth_date = qy.form(
        birth_month=qy.text("Month of birth", validate=validation),
        birth_day=qy.text("Day of birth", validate=validation),
        birth_year=qy.text("Year of birth", validate=year_validation)
    ).ask()
    return birth_date


def prompt_reading_choice():
    reading_choice = qy.select(
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


def prompt_navigation():
    nav_choice = qy.select(
        "Would you like to continue?",
        choices=[
            "Continue",
            "Quit"
        ]
    ).ask()
    return nav_choice


def print_section(section: dict):
    heading = section['heading']
    title = section['title']
    body = section['body_paragraphs']
    tprint(heading, font="thin3")
    print("")
    console.print(title, style="bold")
    print("")
    for paragraph in body:
        console.print(paragraph)
        print("")


def display_heading():
    heading_text = "Numerologoy"
    heading = text2art(heading_text.upper(), font="cybermedium")
    print(heading)


def display_letter_table():
    title = "The way that we do this in numerology, is by using the alphabet conversion chart below:"
    table = Table(title=title)
    # Create table headers
    for number in LETTERS_TABLE:
        table.add_column(number, justify="right", style="cyan", no_wrap=True)
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


def display_app_description():
    heading = APP_DESCRIPTION['heading']
    description = {
        'heading': "Calculate your unique numbers",
        'title': APP_DESCRIPTION['heading'],
        'body_paragraphs': APP_DESCRIPTION['paragraphs']
    }

    print_section(description)


def greet_user(user: dict) -> None:
    first_name = user['first_name']
    middle_name = user['middle_name']
    last_name = user['last_name']
    console.print(f"Hello {first_name} {middle_name} {last_name}", style="bold")


def clear_console() -> None:
    command = 'clear'
    # If Machine is running on Windows, use cls
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
