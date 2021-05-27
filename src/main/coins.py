from exceptions import NotValidCoinValue
from exceptions import ItsNotACoin

from tickets import *
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
    '''Main class for Ticket machine'''
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
            money += key * value

        return money

    def initial_value_of_coin_storage(self, nof_coins, coins_values_list=constants.VALID_COIN_VALUES):
        '''Set initial coin storage of ticket machine'''
        for key in coins_values_list:
            self.set_value(key, nof_coins)

    def print_coins_in_window(self):
        out_stream = ""
        for i in constants.VALID_COIN_VALUES:
            if self.__stored_coins[i] != 0:
                out_stream += str(i / 100.0) + "zł x " + str(self.__stored_coins[i]) + "\n"
        return out_stream

    def stored_money_in_window(self):
        '''print stored money sum in window'''
        if not self.storage_is_empty():
            return "0.0"
        money = 0.0
        for key, value in self.__stored_coins.items():
            if value != 0:
                money += key * value
        return str(money / 100.0)

    def update_stored_coins(self, entered_coins):
        '''update number of stored coins'''
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
            return entered_coins.print_coins_in_window() + " " + constants.CANT_THROW_REST

        else:
            rest_storage = CoinStorage()
            while rest > 0:
                n = 0
                for i in constants.VALID_COIN_VALUES_FOR_LOOP_REVERSE:
                    if rest >= i > n:
                        n = i
                nof_coins = 0
                while rest >= n != 0:
                    rest -= n
                    nof_coins += 1
                if n != 0:
                    rest_storage.set_value(n, rest_storage.__stored_coins[n] + nof_coins)
            tickets.set_zero_tickets_amount()

            for key, value in entered_coins_storage.__stored_coins.items():
                coins_update = coin_storage.__stored_coins.get(key) + (value - rest_storage.__stored_coins.get(key))
                coin_storage.set_value(key, coins_update)
            entered_coins.initial_value_of_coin_storage(0)

            return rest_storage.print_coins_in_window()


coin_storage = CoinStorage()
coin_storage.initial_value_of_coin_storage(10)
entered_coins_storage = CoinStorage()
