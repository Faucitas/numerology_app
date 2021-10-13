import json
import questionary as qy
from textwrap import TextWrapper
from rich.console import Console
from art import tprint
console = Console()

READINGS_DB_URL = 'data/readings.json'

# Load all readings to dict
with open(READINGS_DB_URL, 'r') as file:
    readings_db = json.load(file)


class Reading:
    def __init__(self):
        self.reading = None
        self.number = None
        self.readings = readings_db

    def get_reading(self, reading: dict):
        reading_name = reading['name']
        individual_num = reading['number']
        all_readings = self.readings[reading_name]
        user_reading = all_readings[individual_num]

        reading = {
            'header': user_reading['heading'],
            'body_paragraphs': user_reading['paragraphs']
        }
        self.reading = reading
        return reading

    def print_reading(self):
        reading = self.reading
        # qy.print(reading['header'], style='bold fg:')
        print("")
        for paragraph in reading['body_paragraphs']:
            # self.__print_paragraph(paragraph)
            console.print(paragraph)
            print("")
