import unittest

from coins import *
from exceptions import *


class Tests(unittest.TestCase):
    def test_should_return_no_rest(self):
        tickets_test = Tickets()
        machine = CoinStorage()
        machine.initial_value_of_coin_storage(20)
        tickets_test.add_ticket(1)  # cost = 200
        entered_coins = CoinStorage()
        entered_coins.add_coin(Coin(200))
        self.assertEqual(constants.NO_REST, machine.rest_to_released(entered_coins, tickets_test.chosen_tickets_cost()))

    def test_should_return_rest(self):
        tickets_test = Tickets()
        machine = CoinStorage()
        machine.initial_value_of_coin_storage(20)
        tickets_test.add_ticket(1)  # cost = 200
        entered_coins = CoinStorage()
        entered_coins.add_coin(Coin(200))
        entered_coins.add_coin(Coin(50))
        self.assertEqual("0.5zł x 1\n", machine.rest_to_released(entered_coins, tickets_test.chosen_tickets_cost()))

    def test_should_return_cant_get_rest(self):
        tickets_test = Tickets()
        machine = CoinStorage()
        machine.initial_value_of_coin_storage(1)
        tickets_test.add_ticket(1)  # cost = 200
        entered_coins = CoinStorage()
        entered_coins.add_coin(Coin(5000))
        entered_coins.add_coin(Coin(5000))
        self.assertEqual("50.0zł x 2\n " + constants.CANT_THROW_REST, machine.rest_to_released(entered_coins, tickets_test.chosen_tickets_cost()))

    def test_hundred_coins(self):
        machine = CoinStorage()
        for i in range(100):
            machine.add_coin(Coin(1))
        self.assertEqual(100, machine.stored_money())

    def test_should_return_cost_of_two_tickets(self):
        tickets_test = Tickets()
        tickets_test.add_ticket(1)
        tickets_test.add_ticket(1)
        self.assertEqual(400, tickets_test.chosen_tickets_cost())

    def test_should_return_no_rest_after_insert_tickets_and_money_and_again_tickets_and_again_money(self):  # yas
        tickets_test = Tickets()
        machine = CoinStorage()
        machine.initial_value_of_coin_storage(20)
        tickets_test.add_ticket(1)  # cost = 200
        entered_coins = CoinStorage()
        entered_coins.add_coin(Coin(200))
        tickets_test.add_ticket(2)  # cost = 300
        entered_coins.add_coin(Coin(200))
        entered_coins.add_coin(Coin(100))
        self.assertEqual(constants.NO_REST, machine.rest_to_released(entered_coins, tickets_test.chosen_tickets_cost()))

    def test_should_return_NegativeNumberException(self):
        tickets_test = Tickets()
        with self.assertRaises(NegativeNumber):
            tickets_test.increase_tickets_number("-2")

    def test_should_return_notANumberException(self):
        tickets_test = Tickets()
        with self.assertRaises(NotANumber):
            tickets_test.increase_tickets_number("Not")


if __name__ == '__main__':
    unittest.main()
