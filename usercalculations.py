import json
from user import User
LETTERS_DB = 'data/letters.json'
with open(LETTERS_DB, 'r') as file:
    letters = json.load(file)

LETTER_VALUES = letters['letter_values']
VOWELS = letters['vowels']

class UserCalculations(User):
    def __init__(self,first_name, middle_name, last_name, birth_date):
        super().__init__(first_name, middle_name, last_name, birth_date)
        self.life_path_num = self.__calculate_life_path_num()
        self.soul_urge_num = self.__calculate_soul_urge_num()
        self.expression_num = self.__calculate_expression_num()

    def get_life_path_num(self):
        return self.life_path_num

    def get_soul_urge_num(self):
        return self.soul_urge_num

    def get_expression_num(self):
        return self.expression_num

    def __letters_to_numbers(self, letters):
        return [LETTER_VALUES[letter] for letter in letters]

    def __reduce_numbers(self, numbers):
        sum_numbers = sum(numbers)
        while True:
            if sum_numbers == 11 or sum_numbers == 22:
                return sum_numbers
            elif sum_numbers < 10:
                return sum_numbers
            else:
                reduced_number = 0
                for number in str(sum_numbers):
                    reduced_number += int(number)
                sum_numbers = reduced_number

    def __extract_vowels(self, name):
        vowels_only = ""
        for i in range(0, len(name)):
            current_letter = name[i]
            prior_letter = name[i - 1]
            y_is_a_vowel = self.__is_y_a_vowel(i, prior_letter) if current_letter == 'y' else False
            if y_is_a_vowel or current_letter in VOWELS:
                vowels_only += current_letter
        return vowels_only

    def __is_y_a_vowel(self, cur_letter_index, previous_letter):
        is_first_letter = cur_letter_index == 0
        is_a_vowel = lambda x: x in VOWELS
        if is_first_letter or is_a_vowel(previous_letter):
            return False
        else:
            return True

    def __calculate_life_path_num(self):
        date = self.birth_date
        date_numbers = [int(number) for number in date]
        reduced_num = self.__reduce_numbers(date_numbers)
        return {"name": "life_path", "number": reduced_num}

    def __calculate_soul_urge_num(self):
        letters = ""
        for name in self.full_name:
            vowels_only = self.__extract_vowels(name)
            letters += vowels_only
        letter_values = self.__letters_to_numbers(letters)
        reduced_number = self.__reduce_numbers(letter_values)
        return {"name": "soul_urge", "number": str(reduced_number)}

    def __calculate_expression_num(self):
        full_name = ""
        for name in self.full_name:
            full_name += name
        letter_values = self.__letters_to_numbers(full_name)
        reduced_number = self.__reduce_numbers(letter_values)
        return {"name": "expression", "number": str(reduced_number)}
