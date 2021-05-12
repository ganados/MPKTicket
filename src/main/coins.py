from exceptions import NotValidCoinValue
from exceptions import ItsNotACoin
import constants


class Coin:

    def __init__(self, value):
        if value in constants.VALID_COIN_VALUES:
            self.__value = value
        else:
            raise NotValidCoinValue()

    def get_value(self):
        return self.__value


class CoinStorage:
    def __init__(self):
        self.__nof_entered_coins = 1
        self.__stored_coins = { key: 0 for key in constants.VALID_COIN_VALUES }

    def set_value(self, key, value):
        self.__stored_coins[key] = value

    def add_coin(self, coin):
        if isinstance(coin, Coin):
            self.__stored_coins[coin.get_value()] = self.__nof_entered_coins;
            self.__nof_entered_coins = 1
        else:
            raise ItsNotACoin()

    def initial_value_of_coin_storage(self, nof_coins, coins_values_list=constants.VALID_COIN_VALUES):
        for key in coins_values_list:
            self.set_value(key, nof_coins)


# TODO: dodawanie monet do slownika, wyswietlanie przyjmowanych monet
