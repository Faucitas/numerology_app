class User:
    def __init__(self, full_name, birth_date) -> None:
        self.first_name: str = full_name['first_name']
        self.middle_name: str = full_name['middle_name']
        self.last_name: str = full_name['last_name']
        self.full_name_list = [name.lower() for name in full_name.values()]
        self.birth_date: dict = birth_date

    def get_first_name(self) -> str:
        return self.first_name

    def get_middle_name(self) -> str:
        return self.middle_name

    def get_last_name(self) -> str:
        return self.last_name

    def get_birth_date_str(self) -> str:
        return self.__birth_date_to_str()

    def __birth_date_to_str(self) -> str:
        date_str: str = ""
        date: dict = self.birth_date
        for value in date.values():
            date_str += value

        return date_str
