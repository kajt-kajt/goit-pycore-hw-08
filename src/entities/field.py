class Field:
    """
    Base class for fields in AddressBook. 
    "value" attribute is protected for better control of changes.
    """

    def validate_value(self, value: str) -> str:
        """
        Method for validation and/or normalization of field values.
        General rule - value should be convertible to string.
        It would be a rare situation, but let's check it anyway.
        Subclasses should override it for their type of value.
        Returns sanitized normalized value. Raises ValueError if it is not possible.
        """
        try:
            value_str = str(value)
            return value_str
        except Exception as e:
            input_type = type(value).__name__
            error_msg = f"Field of type {input_type} is not convertible to str, error:\n {e}"
            raise ValueError(error_msg) from e

    def __init__(self, value):
        self._value = self.validate_value(value)

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return f"{self.__class__.__name__}({str(self._value)})"

    def update(self, new_value):
        """
        Update value of field, but validate it first
        """
        self._value = self.validate_value(new_value)
