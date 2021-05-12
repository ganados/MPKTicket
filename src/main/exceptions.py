import constants


class NegativeNumber(Exception):
    def __init__(self):
        super().__init__("Wrong number, works only for positive numbers")
    #   print("Wrong number, works only for positive numbers")


class NotANumber(Exception):
    def __init__(self):
        super().__init__("This is not a number")
    #   print("constants.NOT_A_NUMBER")


class NotAInteger(Exception):
    def __init__(self):
        super().__init__("This is not a Integer")
    #   print(constants.NOT_A_INTEGER)


class NotValidCoinValue(Exception):
    def __init__(self):
        super().__init__("Wrong coin value")
    #   print("Wrong coin value")


class ItsNotACoin(Exception):
    def __init__(self):
        super().__init__("Entered object is not a Coin")
    #   print("Entered object is not a Coin")


class EmptyStorage(Exception):
    def __init__(self):
        super().__init__("Coin storage is empty")
