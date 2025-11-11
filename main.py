"""
Entry point
"""

from collections import defaultdict
from src.handlers import *
from src.entities import AddressBook

def main():
    """
    Main loop for bot
    """

    contacts = AddressBook()

    # command handlers

    def default_handler():
        def inner(*args, **kwargs):
            return "Invalid command."
        return inner

    # all handlers should take 2 arguments - args list and contacts dictionary
    handlers = defaultdict(default_handler, {
        "hello": lambda x,y: "How can I help you?",
        "close": lambda x,y: "Good bye!",
        "exit": lambda x,y: "Good bye!",
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,
        "add-birthday": add_birthday,
        "show-birthday": show_birthday,
        "birthdays": birthdays,
    })

    print("Welcome to the assistant bot!")

    # main loop
    command = ""
    while command not in ["close", "exit"]:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        print(handlers[command](args, contacts))

if __name__ == "__main__":
    main()