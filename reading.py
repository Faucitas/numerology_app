import json

READINGS_DB_URL = 'data/readings.json'

# Load all readings to dict
with open(READINGS_DB_URL, 'r') as file:
    READING_DB = json.load(file)


class Reading:
    def __init__(self):
        self.reading_key = None
        self.reading_num = None
        self.reading_name = None
        self.reading = None
        self.description = None
        self.directions = None

    def get_reading(self,  reading_to_get: dict):
        reading_key = reading_to_get['key']
        reading_num = reading_to_get['number']
        self.__set_reading_values(reading_key, reading_num)
        return self.reading

    def get_description(self, reading_key):
        self.__set_reading_values(reading_key)
        return self.description

    def get_directions(self, reading_key):
        self.__set_reading_values(reading_key)
        return self.directions

    def __set_reading_values(self, reading_key, reading_number: str=None):
        reading_db = READING_DB[reading_key]
        self.reading_key = reading_key
        self.reading_name = reading_db['name']
        self.description = self.__get_description_from_db()
        self.directions = self.__get_directions_from_db()
        if reading_number is not None:
            self.reading_num = reading_number
            self.reading = self.__get_reading_from_db()

    def __get_description_from_db(self):
        description = READING_DB[self.reading_key]['description']
        reading_description = {
            "heading": f"{self.reading_name}",
            "title": description['heading'],
            "body_paragraphs": description['paragraphs']
        }

        return reading_description

    def __get_reading_from_db(self):
        all_readings = READING_DB[self.reading_key]
        user_reading = all_readings['readings'][self.reading_num]
        reading = {
            'heading': f"{self.reading_name} {self.reading_num}",
            'title': user_reading['heading'],
            'body_paragraphs': user_reading['paragraphs']
        }
        return reading

    def __get_directions_from_db(self):
        reading = READING_DB[self.reading_key]
        directions = reading['directions']
        name = reading['name']
        heading = f"How to calculate your {name} number"
        reading_directions = {
            'heading': heading,
            'title': directions['heading'],
            'body_paragraphs': directions['paragraphs']
        }

        return reading_directions
