from typing import *


class User:
    def __init__(self, name: str, email: str, birth_date: str):
        self.name = name
        self.email = email
        self.birth_date = birth_date
        pass

    def __repr__(self) -> str:
        return f'{self.name} ; email: {self.email} ; born: {self.birth_date}'

    pass
