from src.handlers.input_error import input_error
from src.entities import AddressBook

@input_error
def change_contact(args: list[str], contacts: AddressBook) -> str:
    """
    Rewrites record for existing name.
    Returns an error message if contact with given name does not exist.
    "args" should contain 2 values.
    """
    name, old_phone, new_phone = args
    if name not in contacts:
        return f"ERROR: contact '{name}' does not exist!"
    result = contacts[name].edit_phone(old_phone, new_phone)
    return "Contact updated." if result else "Nothing to change."
