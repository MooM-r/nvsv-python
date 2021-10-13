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
                "change user": None,
                "quit": None,
            },
        }

        self.help_infos: Dict = {
            "help": "- displays a list of possible commands",
            "quit": "- Shuts the programm down",
            "add user": "- With this command you can add a user to the list",
            "delete user": "- With this command you can remove a user from the list",
            "save to file": "- With this command you can save all users to a file",
            "load from file": "- With this command you can load users from a file",
            "show user list": "- Shows all users",
            "change user": "- You can hereby choose a user you want to change",
        }

        # self.choices["user_list"]["help"] = self.print_help('user_list')
        # self.choices["user_change"]["help"] = self.print_help('user_change')
        self.choices["main"]["help"] = self.print_help
        self.choices["main"]["add user"] = self.add_user
        self.choices["main"]["delete user"] = self.delete_user
        self.choices["main"]["save to file"] = self.save_users
        self.choices["main"]["load from file"] = self.load_users
        self.choices["main"]["show user list"] = self.show_user_list
        self.choices["main"]["change user"] = self.change_user

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
        print('----------\nWe are here to help!\n\n' + "\n".join((choice.ljust(28, '.')+" " +
              self.help_infos[choice]) for choice in self.choices[level]))
        pass

    def add_user(self) -> None:
        print('---------\nPlease provide the information!\n')
        self.users.append(User(input('Enter the name: '), input(
            'Enter email: '), input('Enter birthdate: ')))
        print(f'\nAdded user:\n{repr(self.users[-1])}\n')
        pass

    def delete_user(self) -> None:
        try:
            self.show_user_list()
            print('-------')
            del_index = int(
                input('Enter the index of the user you want to delete: '))-1
            self.users.pop(del_index)
            print('\n ~ Successfully deleted user ~\n')
        except IndexError:
            print('\n ~ Sorry that index doesn\'t seem to exist ~\n')
        pass

    def save_users(self) -> None:

        if len(self.users) == 0:
            print('\n ~ No users to save… ~\n')
            return

        with open('saved.users', 'wb') as f:
            pickle.dump(self.users, f)
        print('\n ~ Saved users ~\n')
        pass

    def load_users(self) -> None:
        try:
            with open('saved.users', 'rb') as f:
                self.users = pickle.load(f)
            print('\n ~ Loaded users ~\n')
        except Exception:
            print('\n ~ There is no file to load from ~\n')
        pass

    def show_user_list(self) -> None:

        if len(self.users) == 0:
            print('\n ~ Nothing to show here… ~\n')
            return

        print()
        [print(f'{self.users.index(x)+1}. - '+repr(x)+'\n')
         for x in self.users]
        pass

    def change_user(self) -> None:
        self.show_user_list()
        print('-------')
        chng_index = int(input('Which user do you want to change: '))-1

        try:
            tmp = self.users[chng_index]
        except IndexError:
            print('\n ~ Sorry that index doesn\'t seem to exist ~\n')
            return

        name = input(
            'Enter name [in case you don\'t want to change it press ENTER]: ')
        if name == '':
            name = self.users[chng_index].name

        email = input(
            'Enter email [in case you don\'t want to change it press ENTER]: ')
        if email == '':
            email = self.users[chng_index].email

        birthdate = input(
            'Enter birthdate [in case you don\'t want to change it press ENTER]: ')
        if birthdate == '':
            birthdate = self.users[chng_index].birth_date

        self.users.pop(chng_index)
        self.users.insert(chng_index, User(name, email, birthdate))
        print(
            f'\n ~ Succesfully altered the user! ~\nUser is now: {self.users[chng_index]}\n')
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
                print('\n ~ Ey Oi don\'t know that one yet. ~\n')
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
