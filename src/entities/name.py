from src.entities.field import Field

class Name(Field):
    """
    Class for name entity. Is a mandatory field, so may not be empty.
    """

    def validate_value(self, value: str) -> str:
        value_str = super().validate_value(value)
        if not value or not value_str:
            raise ValueError(f"Name value should not be empty: \"{value}\"")
        return value_str
