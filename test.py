"""
Tests to ensure project works correctly
"""

from unittest import main as unittest_main
from unittest import TestCase
from unittest.mock import patch
import io
import sys
from main import main


class TestBot(TestCase):
    """
    TestCase to test bot interactively
    """

    @patch('builtins.input', side_effect=['hello',
                                          'exit'])
    def test_hello(self, mock_input):
        """
        Just hello and exit
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main() ### running main script
        sys.stdout = sys.__stdout__
        ### check all the output
        self.assertEqual(captured_output.getvalue(),
                         "Welcome to the assistant bot!\n"
                         + "How can I help you?\n"
                         + "Good bye!\n")
        ### check input prompts
        for _ in range(2):
            mock_input.assert_called_with("Enter a command: ")


    @patch('builtins.input', side_effect=['add Peter 0123456789',
                                          'all',
                                          'exit'])
    def test_add_contact_all(self, mock_input):
        """
        Add one contact and verify through all that it exists
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main() ### running main script
        sys.stdout = sys.__stdout__
        ### check all the output
        self.assertEqual(captured_output.getvalue(),
                         "Welcome to the assistant bot!\n"
                         + "Contact added.\n"
                         + "Peter: 0123456789\n"
                         + "Good bye!\n")
        ### check input prompts
        for _ in range(3):
            mock_input.assert_called_with("Enter a command: ")


    @patch('builtins.input', side_effect=['add Peter 0123456789',
                                          'phone Peter',
                                          'exit'])
    def test_add_contact_phone(self, mock_input):
        """
        Add new contact and try to get it back with phone
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main() ### running main script
        sys.stdout = sys.__stdout__
        ### check all the output
        self.assertEqual(captured_output.getvalue(),
                         "Welcome to the assistant bot!\n"
                         + "Contact added.\n"
                         + "0123456789\n"
                         + "Good bye!\n")
        ### check input prompts
        for _ in range(3):
            mock_input.assert_called_with("Enter a command: ")


    @patch('builtins.input', side_effect=['add Peter 0123456789',
                                          'add Peter 0123456789',
                                          'add Peter 1234567890',
                                          'phone Peter',
                                          'change Peter 1234567890 0123456789',
                                          'phone Peter',
                                          'exit'])
    def test_add_contact_double_phone(self, mock_input):
        """
        Add new contact, add one more phone and try to get it back with phone
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main() ### running main script
        sys.stdout = sys.__stdout__
        ### check all the output
        self.assertEqual(captured_output.getvalue(),
                         "Welcome to the assistant bot!\n"
                         + "Contact added.\n"*3
                         + "0123456789; 1234567890\n"
                         + "Contact updated.\n"
                         + "0123456789\n"
                         + "Good bye!\n")
        ### check input prompts
        for _ in range(7):
            mock_input.assert_called_with("Enter a command: ")


    @patch('builtins.input', side_effect=['hello',
                                          'HELLO', 
                                          'Hello', 
                                          'Hello ufkjfkd', 
                                          'hello and more', 
                                          'close'])
    def test_hello_misc(self, mock_input):
        """
        Various options for hello: different case, additional parameters etc.
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main() ### running main script
        sys.stdout = sys.__stdout__
        ### check all the output
        self.assertEqual(captured_output.getvalue(),
                         "Welcome to the assistant bot!\n"
                         + "How can I help you?\n"*5
                         + "Good bye!\n")
        ### check input prompts
        for _ in range(6):
            mock_input.assert_called_with("Enter a command: ")


    @patch('builtins.input', side_effect=['add', 
                                          'add Peter', 
                                          'add Peter 123456787 fdfdfd',
                                          'add Peter 12345678', 
                                          'all', 
                                          'exit'])
    def test_add_contact_misc(self, mock_input):
        """
        Wrong number of arguments for add contact
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main() ### running main script
        sys.stdout = sys.__stdout__
        ### check all the output
        self.assertEqual(captured_output.getvalue(),
                         "Welcome to the assistant bot!\n"
                         + "Wrong argument(-s) provided. Try again.\n"*3
                         + "Phone number must be strictly 10 digits, got '12345678' instead.\n"
                         + "\n"
                         + "Good bye!\n")
        ### check input prompts
        for _ in range(5):
            mock_input.assert_called_with("Enter a command: ")

    @patch('builtins.input', side_effect=['gdhgdhs',
                                          'ghghgh jgjj',
                                          '',
                                          'exit'])
    def test_random_input(self, mock_input):
        """
        Strings that are not commands at all.
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main() ### running main script
        sys.stdout = sys.__stdout__
        ### check all the output
        self.assertEqual(captured_output.getvalue(),
                         "Welcome to the assistant bot!\n"
                         + "Invalid command.\n"*3
                         + "Good bye!\n")
        ### check input prompts
        for _ in range(4):
            mock_input.assert_called_with("Enter a command: ")

    @patch('builtins.input', side_effect=['all', 
                                          'phone', 
                                          'phone abcd', 
                                          'phone abcd fgfgfgf', 
                                          'exit'])
    def test_all_phone_misc(self, mock_input):
        """
        all and phone with wrong arguments and empty base
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main() ### running main script
        sys.stdout = sys.__stdout__
        ### check all the output
        self.assertEqual(captured_output.getvalue(),
                         "Welcome to the assistant bot!\n\n"
                         + "Wrong argument(-s) provided. Try again.\n"
                         + "No such contact found.\n"*2
                         + "Good bye!\n")
        ### check input prompts
        for _ in range(5):
            mock_input.assert_called_with("Enter a command: ")


    @patch('builtins.input', side_effect=['add Peter 0123456789',
                                          'change Peter 0123456789 9876543210',
                                          'change Peter 0123456789 9876543210', 
                                          'phone Peter', 
                                          'exit'])
    def test_change(self, mock_input):
        """
        Basic scenario for changing phone number in database
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main() ### running main script
        sys.stdout = sys.__stdout__
        ### check all the output
        self.assertEqual(captured_output.getvalue(),
                         "Welcome to the assistant bot!\n"
                         + "Contact added.\n"
                         + "Contact updated.\n"
                         + "Nothing to change.\n"
                         + "9876543210\n"
                         + "Good bye!\n")
        ### check input prompts
        for _ in range(5):
            mock_input.assert_called_with("Enter a command: ")


    @patch('builtins.input', side_effect=['change',
                                          'change Peter',
                                          'change Peter 987654321',
                                          'change Peter 9876543210',
                                          'change Peter 9876543210 12345',
                                          'change Peter 9876543210 1234567890',
                                          'change Peter 9876543 1234567890',
                                          'all',
                                          'add Peter 0123456789',
                                          'change Peter 23456789',
                                          'change Peter 2345678901',
                                          'change Peter 2345678901 1234',
                                          'change Peter 234567 1234567890',
                                          'change Peter 2345678901 1234567890',
                                          'all',
                                          'change Peter 0123456789 123456',
                                          'all',
                                          'close'])
    def test_change_misc(self, mock_input):
        """
        Various weird scenarios for changing phone number in database
        """
        self.maxDiff = None
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main() ### running main script
        sys.stdout = sys.__stdout__
        ### check all the output
        self.assertEqual(captured_output.getvalue(),
                         "Welcome to the assistant bot!\n"
                         + "Wrong argument(-s) provided. Try again.\n"*4
                         + "ERROR: contact 'Peter' does not exist!\n"*3
                         + "\n"
                         + "Contact added.\n"
                         + "Wrong argument(-s) provided. Try again.\n"*2
                         + "Nothing to change.\n"*3
                         + "Peter: 0123456789\n"
                         + "Phone number must be strictly 10 digits, got '123456' instead.\n"
                         + "Peter: 0123456789\n"
                         + "Good bye!\n")
        ### check input prompts
        for _ in range(18):
            mock_input.assert_called_with("Enter a command: ")    


    @patch('builtins.input', side_effect=['add-birthday',
                                          'add-birthday Peter',
                                          'add-birthday Peter 123 123',
                                          'add-birthday Peter 123',
                                          'all',
                                          'add-birthday Peter 10.11.2026',
                                          'add-birthday Peter 10.11.2020',
                                          'all',
                                          'add Peter 0123456789',
                                          'all',
                                          'close'])
    def test_add_birthday_misc(self, mock_input):
        """
        Various weird scenarios for adding contact birthday
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main() ### running main script
        sys.stdout = sys.__stdout__
        ### check all the output
        self.assertEqual(captured_output.getvalue(),
                         "Welcome to the assistant bot!\n"
                         + "Wrong argument(-s) provided. Try again.\n"*3
                         + "Invalid date format. Use DD.MM.YYYY\n"
                         + "Peter: \n"
                         + "Birth date from future: 10.11.2026\n"
                         + "Birthday information added.\n"
                         + "Peter(10.11.2020): \n"
                         + "Contact added.\n"
                         + "Peter(10.11.2020): 0123456789\n"
                         + "Good bye!\n")
        ### check input prompts
        for _ in range(11):
            mock_input.assert_called_with("Enter a command: ") 


    @patch('builtins.input', side_effect=['birthdays',
                                          'add-birthday Peter 14.11.2020',
                                          'add Peter 0123456789',
                                          'add Peter 0123456789',
                                          'all',
                                          'show-birthday Peter',
                                          'show-birthday Anna',
                                          'add Anna 1234567890',
                                          'show-birthday Anna',
                                          'all',
                                          'add-birthday Anna 12.11.1990',
                                          'birthdays',
                                          'close'])
    def test_birthday(self, mock_input):
        """
        Typical set of operations with birthday
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main() ### running main script
        sys.stdout = sys.__stdout__
        ### check all the output
        self.assertEqual(captured_output.getvalue(),
                         "Welcome to the assistant bot!\n"
                         + "\n"
                         + "Birthday information added.\n"
                         + "Contact added.\n"*2
                         + "Peter(14.11.2020): 0123456789\n"
                         + "14.11.2020\n"
                         + "No such contact found.\n"
                         + "Contact added.\n"
                         + "\n"
                         + "Peter(14.11.2020): 0123456789\n"
                         + "Anna: 1234567890\n"
                         + "Birthday information added.\n"
                         + "[12.11.2025] Anna(12.11.1990): 1234567890\n"
                         + "[14.11.2025] Peter(14.11.2020): 0123456789\n"
                         + "Good bye!\n")
        ### check input prompts
        for _ in range(13):
            mock_input.assert_called_with("Enter a command: ")


    @patch('builtins.input', side_effect=['add Peter 0123456789',
                                          'change Peter 0123456789 1234567890',
                                          'all',
                                          'add Peter 0123456789',
                                          'change Peter 0123456789 1234567890',
                                          'all',
                                          'exit'])
    def test_change_to_duplicate(self, mock_input):
        """
        Various weird scenarios for changing phone number in database
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main() ### running main script
        sys.stdout = sys.__stdout__
        ### check all the output
        self.assertEqual(captured_output.getvalue(),
                         "Welcome to the assistant bot!\n"
                         + "Contact added.\n"
                         + "Contact updated.\n"
                         + "Peter: 1234567890\n"
                         + "Contact added.\n"
                         + "Contact updated.\n"
                         + "Peter: 1234567890\n"
                         + "Good bye!\n")
        ### check input prompts
        for _ in range(7):
            mock_input.assert_called_with("Enter a command: ")


if __name__ == '__main__':
    unittest_main()
