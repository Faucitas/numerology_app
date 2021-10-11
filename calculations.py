import json

LETTERS_DB = 'data/letters.json'
with open(LETTERS_DB, 'r') as file:
    letters = json.load(file)

LETTER_VALUES = letters['letter_values']
VOWELS = letters['vowels']

class Calculations:
    def __init__(self, user):
        self.user = user
        self.merged_full_name = self.__merge_name()
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

    def __string_to_list(self, name):
        return [letter.lower() for letter in name]

    def __merge_name(self):
        first = self.user.first_name
        middle = self.user.middle_name
        last = self.user.last_name
        full_name = first + middle + last
        return full_name.lower()

    def __extract_vowels(self):
        # TODO write function to extract vowels
        pass

    def __is_y_a_vowel(self):
        # TODO write function to descide if why should be treated as a vowel
        pass

    def __calculate_life_path_num(self):
        date = self.user.birth_date
        date_numbers = [int(number) for number in date]
        reduced_num = self.__reduce_numbers(date_numbers)
        return reduced_num

    def __calculate_soul_urge_num(self):
        # TODO write function to calculate soul urge number
        pass

    def __calculate_expression_num(self):
        letters_list = self.__string_to_list(self.merged_full_name)
        letters_to_numbers = self.__letters_to_numbers(letters_list)
        reduced_number = self.__reduce_numbers(letters_to_numbers)
        return reduced_number
