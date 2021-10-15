class User:
    def __init__(self, full_name, birth_date):
        self.first_name = full_name['first_name']
        self.middle_name = full_name['middle_name']
        self.last_name = full_name['last_name']
        self.full_name_list = [name.lower() for name in full_name.values()]
        self.birth_date = birth_date

    def get_first_name(self):
        return self.first_name

    def get_middle_name(self):
        return self.middle_name

    def get_last_name(self):
        return self.last_name

    def get_birth_date_str(self):
        return self.__birth_date_to_str()

    def __birth_date_to_str(self):
        date_str = ""
        date = self.birth_date
        for value in date.values():
            date_str += value

        return date_str