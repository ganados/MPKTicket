
class NegativeNumber(Exception):
    def __init__(self):
        super().__init__("Wrong number, works only for positive numbers")
        print("Wrong number, works only for positive numbers")


class NotValidCoinValue(Exception):
    def __init__(self):
        super().__init__("Wrong coin value")
        print("Wrong coin value")
