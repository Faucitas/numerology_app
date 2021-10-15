import json

READINGS_DB_URL = 'data/readings.json'

# Load all readings to dict
with open(READINGS_DB_URL, 'r') as file:
    READING_DB = json.load(file)


class Reading:
    def __init__(self, reading_to_get: dict):
        self.reading_key = reading_to_get['key']
        self.reading_num = reading_to_get['number']
        self.reading_name = READING_DB[self.reading_key]['name']
        self.reading = self.__get_reading_from_db()
        self.description = self.__get_description_from_db()
        self.directions = self.__get_directions_from_db()


    def get_reading(self):
        return self.reading

    def get_description(self):
        return self.description

    def get_directions(self):
        return self.directions

    def __get_description_from_db(self):
        description = READING_DB[self.reading_key]['description']
        reading_description = {
            "heading": f"{self.reading_name} {self.reading_num}",
            "title": description['heading'],
            "body_paragraphs": description['paragraphs']
        }

        return reading_description

    def __get_reading_from_db(self):
        all_readings = READING_DB[self.reading_key]
        user_reading = all_readings['readings'][self.reading_num]

        reading = {
            'heading': self.reading_name,
            'title': user_reading['heading'],
            'body_paragraphs': user_reading['paragraphs']
        }
        return reading

    def __get_directions_from_db(self):
        directions = READING_DB[self.reading_key]['directions']
        heading = f"How to calculate your {self.reading_name} number"
        reading_directions = {
            'heading': heading,
            'title': directions['heading'],
            'body_paragraphs': directions['paragraphs']
        }

        return reading_directions
