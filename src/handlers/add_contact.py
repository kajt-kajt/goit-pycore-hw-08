from src.handlers.input_error import input_error
from src.entities import AddressBook

@input_error
def add_contact(args: list[str], contacts: AddressBook) -> str:
    """
    Adds new entry to contacts book object. 
    If contact with such name already exists, adds one more phone for that user.
    "args" should contain 2 values.
    """
    name, phone = args
    ## if contact already exists, adding one more phone for user
    if name in contacts:
        contacts[name].add_phone(phone)
    else:
        contacts[name] = phone
    return "Contact added."
