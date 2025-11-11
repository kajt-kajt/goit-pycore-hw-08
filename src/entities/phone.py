from re import fullmatch
from src.entities import Field
from src import CustomValueError

class Phone(Field):
    """
    Class for phone number entity. Value must be 10 numbers.
    """

    def validate_value(self, value: str) -> str:
        """
        Phone numbers must be 10 numbers
        """
        value_str = super().validate_value(value)
        if not fullmatch(r"\d{10}",value_str):
            error_msg = f"Phone number must be strictly 10 digits, got '{value_str}' instead."
            raise CustomValueError(error_msg)
        return value_str