from src.handlers.input_error import input_error
from src.entities import AddressBook, Record

@input_error
def add_birthday(args: list[str], book: AddressBook) -> str:
    """
    Adding birthday information for contact.
    If there is no record with such name, let's create it.
    """
    name, birthdate = args
    if not name in book:
        book.add_record(Record(name))
    book[name].add_birthday(birthdate)
    return "Birthday information added."
