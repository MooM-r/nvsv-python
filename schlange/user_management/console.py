from typing import *
import os
import pwd
from user import User
import pickle


class Console:
    def __init__(self):
        self.users: List = []
        self.choices: Dict = {
            "main": {
                "help": None,
                "add user": None,
                "delete user": None,
                "save to file": None,
                "load from file": None,
                "show user list": None,
                "quit": None,
            },
            # "user_list": {
            #     "help": None,
            #     "change user [index]": None,
            # },
            # "user_change": {
            #     "help": None,
            #     "change name": None,
            #     "change email": None,
            #     "change birthdate": None,
            #     "change most loved function": None,
            # },
        }

        self.help_infos: Dict = {
            "help": "- displays a list of possible commands",
            "quit": "- Shuts the programm down",
            "add user": "- With this command you can add a user to the list",
            "delete user": "- With this command you can remove a user from the list",
            "save to file": "- With this command you can save all users to a file",
            "load from file": "- With this command you can load users from a file",
            "show user list": "- Shows all users",
            "change user [index]": "- You can hereby choose a user you want to change",
            "change name": "- You can change the name of the selected user",
            "change email": "- You can change the email of the selected user",
            "change birthdate": "- You can change the birthdate of the selected user",
            "change most loved function": "- You can change the most loved function of the user",
        }

        # self.choices["user_list"]["help"] = self.print_help('user_list')
        # self.choices["user_change"]["help"] = self.print_help('user_change')
        self.choices["main"]["help"] = self.print_help
        self.choices["main"]["add user"] = self.add_user
        self.choices["main"]["delete user"] = self.delete_user
        self.choices["main"]["save to file"] = self.save_users
        self.choices["main"]["load from file"] = self.load_users
        self.choices["main"]["show user list"] = self.show_user_list

        self.users = []
        pass

    def hello(self):
        print('================================================================\n')
        print('Hi! Welcome ' + self.get_user() +
              ' to the best User management system, you\'ll ever see')
        print('You can try a whole lot here and it\'s really cool!')
        print('Try to appreciate it!')
        print('Have fun!\n')
        print('================================================================\n\n')
        print('By the way… maybe try "help", if you\'re new here\n')
        pass

    def print_help(self, level='main') -> None:
        print('We are here to help!\n' + "\n".join((choice.ljust(28, '.')+" " +
              self.help_infos[choice]) for choice in self.choices[level]))
        pass

    def add_user(self) -> None:
        print('Please provide the information!')
        self.users.append(User(input('Enter the name: '), input(
            'Enter email: '), input('Enter birthdate: ')))
        print(f'\nAdded user:\n{repr(self.users[-1])}')
        pass

    def delete_user(self) -> None:
        try:
            self.users.pop(int(input('Enter user index: ')))
            print('Successfully deleted user')
        except IndexError:
            print('Sorry that index doesn\'t seem to exist')
        pass

    def save_users(self) -> None:
        with open('saved.users', 'wb') as f:
            pickle.dump(self.users, f)
        pass

    def load_users(self) -> None:
        with open('saved.users', 'rb') as f:
            self.users = pickle.load(f)
        pass

    def show_user_list(self) -> None:
        print()
        [print(repr(x)+'\n') for x in self.users]
        pass

    def run(self):

        self.hello()

        running = True

        while running:
            print(f'{self.get_user()} ~', end=' ')
            user_input = input()

            if user_input == 'quit':
                running = False
                print(f'\nBye {self.get_user()}!\n')
                break

            if not user_input in self.choices["main"].keys():
                continue

            self.choices["main"][user_input]()

            pass
        pass

    def get_user(self) -> str:
        return pwd.getpwuid(os.getuid())[0]
    pass


def main():
    console = Console()
    vars(console)
    console.run()
    pass


if __name__ == '__main__':
    main()
