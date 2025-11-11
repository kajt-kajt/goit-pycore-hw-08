from src.entities import Name, Phone, Birthday

class Record:
    """
    Class representing a single record in address book with name and a list of phone numbers.
    """
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        birthday_info = self.get_birthday()
        if birthday_info:
            birthday_info = f"({birthday_info})"
        return f"{self.name}{birthday_info}: {'; '.join(str(p) for p in self.phones)}"

    def __repr__(self):
        return f"Record({str(self)})"

    def add_phone(self, phone: str):
        """
        Add phone number to list for this record
        """
        if not self.find_phone(phone):
            self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        """
        Remove phone number from list for this record
        """
        self.phones = [phone_record for phone_record in self.phones if str(phone_record) != phone]

    def edit_phone(self, old_phone: str, new_phone: str) -> bool:
        """
        Find phone number record in the list and update it with new value.
        Returns True if old number was found and replaced.
        Also function removes potential duplicates that might occur due to changes.
        """
        # also removing potential duplicates
        temp_list = []
        new_phones = []
        update_took_place = False
        for phone_record in self.phones:
            phone_record_str = str(phone_record)
            if str(phone_record) == old_phone:
                phone_record.update(new_phone)
                phone_record_str = str(phone_record)
                update_took_place = True
            if phone_record_str not in temp_list:
                temp_list.append(phone_record_str)
                new_phones.append(phone_record)
        self.phones = new_phones
        return update_took_place


    def find_phone(self, phone: str) -> Phone | None:
        """
        Find phone number in the list
        """
        result = None
        for phone_record in self.phones:
            if str(phone_record) == phone:
                result = phone_record
                break
        return result

    def get_phones(self) -> str:
        """
        Output all phone numbers in record
        """
        return '; '.join(str(p) for p in self.phones)

    def add_birthday(self, birthdate: str | None):
        """
        Add or update birthday field of the record
        """
        if birthdate is None:
            self.birthday = None
        else:
            self.birthday = Birthday(birthdate)
    
    def get_birthday(self) -> str:
        """
        Display birthday information for contact
        """
        if self.birthday is None:
            return ""
        return str(self.birthday)
