from datetime import datetime
from src.entities import Field
from src import CustomValueError


class Birthday(Field):
    """
    Class for field with birth date of contact
    """

    def validate_value(self, value: str) -> datetime:
        """
        For this field value should be valid date in format DD.MM.YYYY
        """
        birthdate = None
        try:
            birthdate = datetime.strptime(value, "%d.%m.%Y").date()
            if birthdate > datetime.now().date():
                raise CustomValueError(f"Birth date from future: {value}")
        except CustomValueError as e:
            raise e
        except ValueError as e:
            raise CustomValueError("Invalid date format. Use DD.MM.YYYY") from e
        return birthdate

    def __str__(self):
        if self._value:
            return self._value.strftime("%d.%m.%Y")
        return ""
    
    def get_birthday_as_date(self):
        """
        This method returns birthday as datetime date
        """
        return self._value
