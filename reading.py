import json

READINGS_DB_URL: str = 'data/readings.json'

# Load all readings to dict
with open(READINGS_DB_URL, 'r') as file:
    READING_DB = json.load(file)


class Reading:
    def __init__(self):
        self.reading_key: str = ""
        self.reading_num: str = ""
        self.reading_name: str = ""
        self.reading: dict = {}
        self.description: dict = {}
        self.directions: dict = {}

    def get_reading(self,  reading_to_get: dict) -> dict:
        reading_key: str = reading_to_get['key']
        self.reading_num = reading_to_get['number']
        self.__set_reading_values(reading_key)
        return self.reading

    def get_description(self, reading_key) -> dict:
        self.__set_reading_values(reading_key)
        return self.description

    def get_directions(self, reading_key) -> dict:
        self.__set_reading_values(reading_key)
        return self.directions

    def __set_reading_values(self, reading_key) -> None:
        reading_db: dict = READING_DB[reading_key]
        self.reading_key = reading_key
        self.reading_name = reading_db['name']
        self.description = self.__get_description_from_db()
        self.directions = self.__get_directions_from_db()
        if self.reading_num != "":
            self.reading = self.__get_reading_from_db()

    def __get_description_from_db(self) -> dict:
        description: dict = READING_DB[self.reading_key]['description']
        reading_description: dict = {
            "heading": f"{self.reading_name}",
            "title": description['heading'],
            "body_paragraphs": description['paragraphs']
        }

        return reading_description

    def __get_reading_from_db(self) -> dict:
        all_readings: dict = READING_DB[self.reading_key]
        user_reading: dict = all_readings['readings'][self.reading_num]
        reading: dict = {
            'heading': f"{self.reading_name} {self.reading_num}",
            'title': user_reading['heading'],
            'body_paragraphs': user_reading['paragraphs']
        }
        return reading

    def __get_directions_from_db(self) -> dict:
        reading: dict = READING_DB[self.reading_key]
        directions: dict = reading['directions']
        name: str = reading['name']
        heading: str = f"How to calculate your {name} number"
        reading_directions: dict = {
            'heading': heading,
            'title': directions['heading'],
            'body_paragraphs': directions['paragraphs']
        }

        return reading_directions
