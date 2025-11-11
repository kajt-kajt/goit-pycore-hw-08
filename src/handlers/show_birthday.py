from src.handlers.input_error import input_error
from src.entities import AddressBook

@input_error
def show_birthday(args: list[str], book: AddressBook):
    """
    Returns birthday for given name.
    Returns an error message if contact with such name is absent.
    """
    name = args[0]
    return book[name].get_birthday()

