from exceptions import NotValidCoinValue


class Coin:
    valid_coin_values = {0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0}

    def __init__(self, value):
        if value in self.valid_coin_values:
            self.__value = value
        else:
            raise NotValidCoinValue()

    def get_value(self):
        return self.__value


class CoinStorage:
    def __init__(self):
        self.__entered_coins = 1
        self.__stored_coins = {}

