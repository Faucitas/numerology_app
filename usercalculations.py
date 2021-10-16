import json
from user import User

LETTERS_DB = 'data/app_data.json'
with open(LETTERS_DB, 'r') as file:
    LETTERS: dict = json.load(file)

LETTER_VALUES: dict = LETTERS['letter_values']
VOWELS: dict = LETTERS['vowels']


class UserCalculations(User):
    def __init__(self, full_name, birth_date) -> None:
        super().__init__(full_name, birth_date)
        self.life_path_num: dict = self.__calculate_life_path_num()
        self.soul_urge_num: dict = self.__calculate_soul_urge_num()
        self.expression_num: dict = self.__calculate_expression_num()

    def get_reading_num(self, reading_key: str) -> dict:
        number: dict = {}
        if reading_key == 'life_path':
            number = self.life_path_num
        elif reading_key == 'soul_urge':
            number = self.soul_urge_num
        elif reading_key == 'expression':
            number = self.expression_num

        return number

    def __letters_to_numbers(self, letters: str) -> list:
        return [LETTER_VALUES[letter] for letter in letters]

    def __reduce_numbers(self, numbers: list) -> str:
        numbers_sum: int = sum(numbers)
        while True:
            if numbers_sum == 11 or numbers_sum == 22:
                return str(numbers_sum)
            elif numbers_sum < 10:
                return str(numbers_sum)
            else:
                reduced_number = 0
                for number in str(numbers_sum):
                    reduced_number += int(number)
                numbers_sum = reduced_number

    def __extract_vowels(self, name: str) -> str:
        """Loops through a name and returns a string of only the vowels"""
        vowels_only: str = ""
        for i in range(0, len(name)):
            current_letter: str = name[i]
            prior_letter: str = name[i - 1]
            y_is_a_vowel: bool = self.__is_y_a_vowel(i, prior_letter) if current_letter == 'y' else False
            if y_is_a_vowel or current_letter in VOWELS:
                vowels_only += current_letter
        return vowels_only

    def __is_y_a_vowel(self, cur_letter_index: int, previous_letter: str) -> bool:
        """
        Checks if y is a treated as a vowel based on the weather
        it is the first letter or the letter prior is a consonant or not
        """
        is_first_letter: bool = cur_letter_index == 0
        if is_first_letter or previous_letter in VOWELS:
            return False
        else:
            return True

    def __calculate_life_path_num(self) -> dict:
        date: str = self.get_birth_date_str()
        date_numbers: list = [int(number) for number in date]
        reduced_num: str = self.__reduce_numbers(date_numbers)
        return {"key": "life_path", "number": reduced_num}

    def __calculate_soul_urge_num(self) -> dict:
        letters: str = ""
        # Extract the vowels from the first, middle, and last name
        for name in self.full_name_list:
            vowels_only = self.__extract_vowels(name)
            letters += vowels_only
        # Covert letters to numbers based on pre defined table
        letter_values: list = self.__letters_to_numbers(letters)
        reduced_number: str = self.__reduce_numbers(letter_values)
        return {"key": "soul_urge", "number": reduced_number}

    def __calculate_expression_num(self) -> dict:
        full_name: str = ""
        for name in self.full_name_list:
            full_name += name
        letter_values: list = self.__letters_to_numbers(full_name)
        reduced_number: str = self.__reduce_numbers(letter_values)
        return {"key": "expression", "number": reduced_number}
