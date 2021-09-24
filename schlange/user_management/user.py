from typing import *

class User:
    def __init__(self, name:str, email:str, birth_date:str, most_loved_function:function):
        self.name = name
        self.email = email
        self.birth_date = birth_date
        self.most_loved_function = most_loved_function
        pass

    def __str__(self):
        print(f'Username: {self.name}\nEmail: {self.email}\nBirth Date: {self.birth_date}\nMost loved Function: {self.most_loved_function.text}')
        pass
    pass