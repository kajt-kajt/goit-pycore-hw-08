from src.handlers.input_error import input_error
from src.entities import AddressBook

@input_error
def birthdays(_: list[str], book: AddressBook):
    """
    Display list of contacts for greeting during next week
    """
    upcoming_birthdays = book.get_upcoming_birthdays()
    upcoming_birthdays.sort(key=lambda x: x["congratulation_date"])
    result = "\n".join([f"[{x["congratulation_date"].strftime("%d.%m.%Y")}] {str(x["record"])}"
                        for x in upcoming_birthdays])
    return result

