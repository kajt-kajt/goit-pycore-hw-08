from datetime import datetime, date, timedelta
from collections import UserDict
from src.entities import Record

class AddressBook(UserDict):
    """
    Class for address book entity, extends dict, so has its main object in data field.
    Key for the dictionary would be name as str for easier search.
    """

    def __setitem__(self, key, item):
        """
        If item to add is not of class Record - let's convert it to Record
        """
        if isinstance(item, Record):
            # value is Record, some internal call
            return super().__setitem__(key, item)
        else:
            # new name
            value = Record(key)
            value.add_phone(item)
            return super().__setitem__(key, value)

    def add_record(self, record: Record):
        """
        Add record to address book. If such name already exists, record will be rewritten.
        """
        if not isinstance(record, Record):
            error_msg = f"Expecting object of type Record, but got {type(record).__name__} instead."
            raise ValueError(error_msg)
        self[str(record.name)] = record

    def find(self, name: str) -> Record:
        """
        Get record by name. Return None if record with such name does not exist.
        """
        return self.get(name)

    def delete(self, name:str) -> Record:
        """
        Delete record from address book by name and return it back. 
        Return None if record was not found.
        """
        return self.pop(name, None)

    def get_upcoming_birthdays(self) -> list[dict[str,str]]:
        """
        Generate the list of birthday greetings for upcoming week
    
        If this year's birthday of a person is Saturday or Sunday, 
            greeting day is moved to next Monday.
        """
        users = [{ "record": record, "birthday": record.birthday}
                 for record in self.values() if record.birthday is not None]
        result = []
        today_date = datetime.today().date()
        for user in users:
            user_birthdate = user["birthday"].get_birthday_as_date()
            # Substitute year to current one to get first estimate of congratulation date
            user_congratulation_day = date(year=today_date.year,
                                           month=user_birthdate.month,
                                           day=user_birthdate.day)
            # If user already had birthday this year, move his congratulation date to next year
            if user_congratulation_day < today_date:
                user_congratulation_day = date(year=(today_date.year + 1),
                                               month=user_birthdate.month,
                                               day=user_birthdate.day)
            # If user's congratulation date is Saturday, let's move it on Monday
            if user_congratulation_day.weekday() == 5: 
                user_congratulation_day = user_congratulation_day + timedelta(days=2)
            # If user's congratulation date is Sunday, let's move it on Monday
            if user_congratulation_day.weekday() == 6: 
                user_congratulation_day = user_congratulation_day + timedelta(days=1)
            # If user's congratulation date is within a week, let's add him to output
            if (user_congratulation_day - today_date) < timedelta(days=7):
                result.append({
                    "record": user["record"],
                    "congratulation_date": user_congratulation_day
                    })
        return result

