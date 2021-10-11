import json
import questionary as qy
from textwrap import TextWrapper

READINGS_DB = 'data/readings.json'
tw = TextWrapper()

# Load all readings to dict
with open(READINGS_DB, 'r') as file:
    readings = json.load(file)


class Reading:
    def __init__(self):
        self.reading = None
        self.number = None
        self.readings = readings

    def get_reading(self, reading_name, individual_num):
        all_readings = self.readings[reading_name]
        user_reading = all_readings[individual_num]

        reading = {
            'header': user_reading['heading'],
            'body_paragraphs': user_reading['paragraphs']
        }
        self.reading = reading
        return reading

    def __print_paragraph(self, paragraph):
        wrapped_paragraph = tw.wrap(paragraph)
        for line in wrapped_paragraph:
            print(line)

    def print_reading(self):
        reading = self.reading
        qy.print(reading['header'], style='bold underline')
        for paragraph in reading['body_paragraphs']:
            self.__print_paragraph(paragraph)
            print("")
