import tkinter as tk
from tkinter import *
from tkinter import ttk
from coins import *


class Gui:
    def __init__(self):
        window = Tk()
    #   window.geometry("210x300")
        window.title("MPK machine")
        mainframe = ttk.Frame(window)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Label(mainframe, text="Automat MPK", font=("Times New Roman", "16"), foreground="BLUE").grid(columnspan=4, row=0)

        ttk.Label(mainframe, text="\t", font=("Times New Roman", "14")).grid(column=1, rowspan=10)

    #   Wybór biletów
        ttk.Label(mainframe, text="Wybierz i dodaj bilet").grid(column=0, row=1)
        ttk.Button(mainframe, width=20, text="Bilet ulgowy 20 min", command=lambda: tickets.add_ticket(1)).grid(column=0, row=2)
        ttk.Button(mainframe, width=20, text="Bilet normalny 20 min", command=lambda: tickets.add_ticket(2)).grid(column=0, row=3)
        ttk.Button(mainframe, width=20, text="Bilet ulgowy 40 min", command=lambda: tickets.add_ticket(3)).grid(column=0, row=4)
        ttk.Button(mainframe, width=20, text="Bilet normalny 40 min", command=lambda: tickets.add_ticket(4)).grid(column=0, row=5)
        ttk.Button(mainframe, width=20, text="Bilet ulgowy 60 min", command=lambda: tickets.add_ticket(5)).grid(column=0, row=6)
        ttk.Button(mainframe, width=20, text="Bilet normalny 60 min", command=lambda: tickets.add_ticket(6)).grid(column=0, row=7)

    #   Wyświetlenie cennika
        ttk.Button(mainframe, width=20, text="Cennik", command=lambda: self.ticket_price_window()).grid(column=2, row=2, rowspan=6)
        ttk.Label(mainframe, text="").grid(column=0, row=8)

    #   Wyświetlenie wybranych biletów i ewentualne zresetowanie wyboru
        ttk.Button(mainframe, width=30, text="Pokaż wybrane bilety", command=lambda: self.chosen_tickets_window()).grid(column=0, row=9)
        ttk.Button(mainframe, width=30, text="Usuń wybór biletów", command=lambda: tickets.set_zero_tickets_amount()).grid(column=0, row=10)
        ttk.Button(mainframe, width=30, text="Kwota do zapłaty", command=lambda: self.chosen_tickets_cost_window()).grid(column=0, row=11)

    #   Wprowadzenie ilości biletów
        ttk.Label(mainframe, text="Ile biletow chcesz kupić? (domyślnie 1)").grid(column=2, row=10)
        enter_number = Entry(mainframe)
        enter_number.grid(column=2, row=11)
        ttk.Button(mainframe, width=20, text="Wprowadz", command=lambda: tickets.increase_tickets_number(enter_number.get())).grid(column=2, row=12)

    #   Płatność
        ttk.Button(mainframe, width=20, text="Zatwierdź i zapłać", command=lambda: self.accept_and_pay(self)).grid(column=2, row=13)

        window.mainloop()

    @staticmethod
    def ticket_price_window():
        window_ticket_price = Tk()
        window_ticket_price.geometry("200x200")
        window_ticket_price.title("Cennik")
        mainframe = ttk.Frame(window_ticket_price)
        mainframe.grid(column=1, row=1, sticky=(N, W, E, S))
        ttk.Label(mainframe, text=tickets.print_tickets_in_window(), font=("Times New Roman", "14")).grid(column=1, row=0)
        ttk.Button(mainframe, text="Zamknij", command=lambda: window_ticket_price.destroy()).grid(column=1, row=1)

    @staticmethod
    def chosen_tickets_window():
        window_ticket_chosen = Tk()
        window_ticket_chosen.title("Wybrane bilety")
        mainframe = ttk.Frame(window_ticket_chosen)
        mainframe.grid(column=1, row=1, sticky=(N, W, E, S))
        ttk.Label(mainframe, text=tickets.chosen_tickets_in_window(), font=("Times New Roman", "14")).grid(column=1, row=0)
        ttk.Button(mainframe, text="Zamknij", command=lambda: window_ticket_chosen.destroy()).grid(column=1, row=1)

    @staticmethod
    def chosen_tickets_cost_window():
        window_ticket_price = Tk()
        window_ticket_price.title("Koszt")
        mainframe = ttk.Frame(window_ticket_price)
        mainframe.grid(column=1, row=1, sticky=(N, W, E, S))
        ttk.Label(mainframe, text=tickets.chosen_tickets_cost_in_window(), font=("Times New Roman", "14")).grid(column=1, row=0)
        ttk.Button(mainframe, text="Zamknij", command=lambda: window_ticket_price.destroy()).grid(column=1, row=1)

    @staticmethod
    def accept_and_pay(self):
        window_ticket_pay = Tk()
        window_ticket_pay.title("Płatność")
        mainframe = ttk.Frame(window_ticket_pay)
        mainframe.grid(column=1, row=1, sticky=(N, W, E, S))
        i = 2
        for value in constants.VALID_COIN_VALUES_FOR_LOOP:
            ttk.Button(mainframe, width=20, text="Wrzuć " + str(value / 100.0) + "zł", command=lambda coin_value=value: entered_coins_storage
                       .add_coin(Coin(coin_value))).grid(column=2, row=i)
            i += 1
        ttk.Label(mainframe, text="Ile monet chcesz wrzucić? (domyślnie 1)").grid(column=2, row=i+1)
        enter_number = Entry(mainframe)
        enter_number.grid(column=2, row=i+2)
        ttk.Button(mainframe, width=20, text="Wprowadz", command=lambda: entered_coins_storage.increase_coins_number(enter_number.get())).grid(column=2, row=i+3)
        ttk.Button(mainframe, width=20, text="Wprowadzona kwota", command=lambda: self.print_money(entered_coins_storage)).grid(column=2, row=i+4)
        ttk.Button(mainframe, width=20, text="Zapłać", command=lambda: self.pay()).grid(column=2, row=i+5)

    @staticmethod
    def pay():
        window_pay = Tk()
        window_pay.title("Zapłacono")
        mainframe = ttk.Frame(window_pay)
        mainframe.grid(column=1, row=1, sticky=(N, W, E, S))

        ttk.Label(mainframe, text="Zapłacono: ").grid(column=1, row=1)
        ttk.Label(mainframe, text=entered_coins_storage.stored_money_in_window() + "zł").grid(column=2, row=1)
        ttk.Label(mainframe, text="Wartość biletów: ").grid(column=1, row=2)
        ttk.Label(mainframe, text=tickets.chosen_tickets_cost_in_window()).grid(column=2, row=2)
        ttk.Label(mainframe, text="Reszta: ").grid(column=1, row=3)
        ttk.Label(mainframe, text=coin_storage.rest_to_released(entered_coins_storage, tickets.chosen_tickets_cost())).grid(column=2, row=3)

    @staticmethod
    def print_money(entered_coins):
        window_print_money = Tk()
        window_print_money.title("Wpłacona kwota")
        mainframe = ttk.Frame(window_print_money)
        mainframe.grid(column=1, row=1, sticky=(N, W, E, S))
        ttk.Label(mainframe, text=(entered_coins.stored_money_in_window()+"zł"), font=("Times New Roman", "14")).grid(column=1, row=0)

        ttk.Button(mainframe, text="Zamknij", command=lambda: window_print_money.destroy()).grid(column=1, row=2)

# TODO: Obsluga platnosci, wysw
