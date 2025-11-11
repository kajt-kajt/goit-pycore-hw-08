from src.handlers.input_error import input_error

@input_error
def parse_input(user_input: str) -> tuple[str,list[str]]:
    """
    Parses user input into command and arguments.
    """
    cmd, *args = user_input.strip().split()
    cmd = cmd.strip().lower()
    return cmd, *args
