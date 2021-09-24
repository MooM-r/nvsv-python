from typing import *


class Console:
    def __init__(self):
        self.users: List = []
        self.choices: Dict = {
            "main": {
                "help": print(f'We\'re here to help!\n{"\n".join((choice+" "+self.help_infos[choice]) for choice in self.choices["main"])}'),
            },
            "user_list": "",
            "user_change": "",
        }
        self.help_infos: Dict = {
            "help": "displays a list of possible commands",
        }
        pass

    def hello(self):
        print('================================================================\n')
        print('Welcome to the best User management system, you\'ll ever see')
        print('You can try a whole lot here and it\'s really cool!')
        print('Try to appreciate it!')
        print('Have fun!\n')
        print('================================================================\n\n\n\n')
        print('By the way… maybe try "help", if you\'re new here\n\n')
        pass

    def print_choices(self, depth: int = 0) -> int:
        print('What do you want to do?')
        return choice

    def run(self):

        pass
    pass
