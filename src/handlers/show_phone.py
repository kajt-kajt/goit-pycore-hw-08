from src.handlers.input_error import input_error
from src.entities import AddressBook

@input_error
def show_phone(args: list[str], contacts: AddressBook) -> str:
    """
    Returns phone for given name.
    Returns an error message if contact with such name is absent.
    """
    name = args[0]
    return contacts[name].get_phones()
