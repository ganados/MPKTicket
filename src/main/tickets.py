from exceptions import NegativeNumber
from exceptions import NotANumber
import constants


class Tickets:
    def __init__(self):
        self.__tickets_number = 1
        self.__tickets_ids = {
            1: "20 min ulgowy",
            2: "20 min normalny",
            3: "40 min ulgowy",
            4: "40 min normalny",
            5: "60 min ulgowy",
            6: "60 min normalny"
        }
        self.__tickets_price = {
            1: 200,
            2: 300,
            3: 350,
            4: 450,
            5: 500,
            6: 650
        }
        self.__tickets_amount = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0
        }

    def get_ticket_name(self, key):
        return self.__tickets_ids.get(key)

    def get_ticket_amount(self, key):
        return self.__tickets_amount.get(key)

    def get_ticket_price(self, key):
        return self.__tickets_price.get(key)

    def get_number_of_ticket_types(self):
        return len(self.__tickets_ids)

    def set_ticket_number(self, key, value):
        self.__tickets_amount[key] = value

    def chosen_tickets(self):
        '''Printing chosen tickets'''
        for i in range(1, self.get_number_of_ticket_types() + 1):
            print(self.get_ticket_name(i), ": ", self.get_ticket_amount(i))

    def increase_tickets_number(self, value):
        '''Increase tickets number to input to machine'''
        if not value.strip()[1:].isdigit():
            raise NotANumber()
        value = int(value)
        if value < 0:
            raise NegativeNumber()
        self.__tickets_number = value

    def set_zero_tickets_amount(self):
        '''Delete all tickets'''
        for i in range(1, self.get_number_of_ticket_types() + 1):
            self.__tickets_amount[i] = 0

    def add_ticket(self, chosen_ticket):
        '''Add tickets to machine'''
        if chosen_ticket in self.__tickets_ids.keys():
            self.__tickets_amount[chosen_ticket] += self.__tickets_number
        else:
            print(constants.WRONG_CHOSEN_TICKET)
        self.__tickets_number = 1

# for display in the window
    def chosen_tickets_cost(self):
        '''Calculate chosen tickets cost'''
        cost = 0.0
        for i in range(1, self.get_number_of_ticket_types() + 1):
            cost += self.get_ticket_price(i) * self.get_ticket_amount(i)
#        print("Tickets cost: ", cost)
        return cost

    def print_tickets_in_window(self):
        '''For printing all tickets in gui'''
        stream_out = ""
        for i in range(1, self.get_number_of_ticket_types() + 1):
            stream_out += str(self.get_ticket_name(i)) + " " + str(self.get_ticket_price(i)) + "0z??\n"
        return stream_out

    def chosen_tickets_in_window(self):
        '''For printing chosen tickets in gui'''
        stream_out = ""
        for i in range(1, self.get_number_of_ticket_types() + 1):
            stream_out += str(self.get_ticket_name(i)) + ": " + str(self.get_ticket_amount(i)) + "\n"
        return stream_out

    def chosen_tickets_cost_in_window(self):
        '''Chosen tickets cost in window'''
        cost = 0.0
        for i in range(1, self.get_number_of_ticket_types() + 1):
            cost += self.get_ticket_price(i) * self.get_ticket_amount(i)
        #        print("Tickets cost: ", cost)
        return str(cost / 100.0) + "0z??"


tickets = Tickets()
