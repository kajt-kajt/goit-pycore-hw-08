from src.entities import AddressBook

def show_all(_, contacts: AddressBook) -> str:
    """
    Outputs all the contents of in-memory database of contacts.
    """
    result = [f"{contacts[name]}" for name in contacts]
    return "\n".join(result)
