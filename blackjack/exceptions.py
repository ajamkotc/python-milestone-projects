class InsufficientFundsException(Exception):
    "Bet amount is greater than available funds"
    pass

class InputException(Exception):
    "Invalid menu choice"
    pass

class InvalidNameException(Exception):
    "Raised when the inputted name is invalid"
    pass