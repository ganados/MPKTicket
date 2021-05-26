from exceptions import NotValidCoinValue
from exceptions import ItsNotACoin
from exceptions import EmptyStorage

from tickets import *
import constants


class Coin:

    def __init__(self, value):
        if float(value) in constants.VALID_COIN_VALUES:
            self.__value = float(value)
        else:
            raise NotValidCoinValue()

    def get_value(self):
        return self.__value


class CoinStorage:
    def __init__(self):
        self.__nof_entered_coins = 1
        self.__stored_coins = {key: 0 for key in constants.VALID_COIN_VALUES}

    def set_value(self, key, value):
        self.__stored_coins[key] = value

    def add_coin(self, coin):
        if isinstance(coin, Coin):
            temp = self.stored_coin_by_value(coin.get_value())
            temp += self.__nof_entered_coins
            self.__stored_coins.update({coin.get_value(): temp})
            self.__nof_entered_coins = 1
        else:
            raise ItsNotACoin()

    def increase_coins_number(self, value):
        if not value.strip().isdigit():
            raise NotANumber()
        value = int(value)
        if value < 0:
            raise NegativeNumber
        self.__nof_entered_coins = value

    def stored_coin_by_value(self, key):
        return self.__stored_coins[key]

    def storage_is_empty(self):
        count = 0
        for value in self.__stored_coins.values():
            count += value
        return count

    def stored_money(self):
        if not self.storage_is_empty():
            return 0.0
        money = 0.0
        for key, value in self.__stored_coins.items():
            money += float(key) * float(value)

        return money

    def initial_value_of_coin_storage(self, nof_coins, coins_values_list=constants.VALID_COIN_VALUES):
        for key in coins_values_list:
            self.set_value(key, nof_coins)

    def print_coins_in_window(self):
        out_stream = ""
        for i in constants.VALID_COIN_VALUES:
            out_stream += str(i) + " " + str(self.__stored_coins[i]) + "\n"
        return out_stream

    def stored_money_in_window(self):
        if not self.storage_is_empty():
            return "0.0"
        money = 0.0
        for key, value in self.__stored_coins.items():
            money += key * value
        return str(money)

    def update_stored_coins(self, entered_coins):
        for key in self.__stored_coins.keys():
            self.__stored_coins[key] += entered_coins.stored_coin_by_value(key)

    def rest_to_released(self, entered_coins, tickets_cost):
        entered_money = entered_coins.stored_money()
        rest = entered_money - tickets_cost
        print(rest)
        if entered_money < tickets_cost:
            return constants.NOT_ENOUGH

        elif entered_money == tickets_cost:
            self.update_stored_coins(entered_coins)
            tickets.set_zero_tickets_amount()
            return constants.NO_REST

        elif rest > self.stored_money():
            tickets.set_zero_tickets_amount()
            return entered_coins.stored_money_in_window() + " Nie mogę wydać reszty"

        else:
            rest_storage = CoinStorage()
            temp = rest
            while rest_storage.stored_money() < rest:
                for i in constants.VALID_COIN_VALUES_REVERSE:
                    nof_coins = 0
                    if temp % i == 0:
                        nof_coins += temp / i
                        temp /= i
                        rest_storage.set_value(i, nof_coins)
                        print(rest_storage.stored_money())
            tickets.set_zero_tickets_amount()

            for key, value in entered_coins_storage.__stored_coins.items():
                coins_update = coin_storage.__stored_coins.get(key) - entered_coins_storage.__stored_coins.get(key)
                coin_storage.set_value(key, coins_update)
                entered_coins.initial_value_of_coin_storage(0)

            return rest_storage.stored_money_in_window()


coin_storage = CoinStorage()
coin_storage.initial_value_of_coin_storage(10)
entered_coins_storage = CoinStorage()
