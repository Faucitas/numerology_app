class User:
    def __init__(self, first_name, middle_name, last_name, birth_date):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.full_name = [first_name, middle_name, last_name]
        self.birth_date = birth_date

    def get_first_name(self):
        return self.first_name

    def get_middle_name(self):
        return self.middle_name

    def get_last_name(self):
        return self.last_name

    def get_birt_date(self):
        return self.birth_date