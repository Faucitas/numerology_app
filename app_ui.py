import questionary as qy
from art import text2art, tprint
from rich.console import Console
from questionary import Separator
console = Console()

def display_heading():
    heading_text = {
        "heading": "Numerologoy",
        "sub_heading": "Calculate your unique numbers"
    }
    heading = text2art(heading_text['heading'].upper(), font="cybermedium")
    sub_heading = text2art(heading_text['sub_heading'   ], font="thin3")
    print(heading)
    print(sub_heading)


def prompt_user_name():
    validation = lambda text: True if text.isalpha() else "Please enter only letters"
    qy.print("Please enter your full birth name", style="bold fg:orange")
    user: object = qy.form(
        first_name = qy.text("First name", validate=validation),
        middle_name = qy.text("Middle name", validate=validation),
        last_name = qy.text("Last name", validate=validation)
    ).ask()
    return user


def prompt_birth_date():
    validation = lambda text: True if text.isdigit() else "Please enter the a number"
    year_validation = lambda text: True if len(text) == 4 else "Enter 4 digit year"
    birth_date = qy.form(
        birth_month = qy.text("Month of birth", validate=validation),
        birth_day = qy.text("Day of birth", validate=validation),
        birth_year = qy.text("Year of birth", validate=year_validation)
    ).ask()
    return birth_date


def prompt_reading_choice():
    reading_choice = qy.select(
        "Choose a reading",
        choices=[
            "Life Path Number",
            "Soul Urge Number",
            "Expression Number"
        ]
    ).ask()

    return reading_choice


def prompt_navigation():
    nav_choice = qy.select(
        "What would you like to do",
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