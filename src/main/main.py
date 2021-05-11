from tickets import Tickets

ticket = Tickets()
ticket.set_ticket_number(2, 2)
ticket.set_ticket_number(3, 1)

ticket.chosen_tickets()
ticket.chosen_tickets_cost()
print(ticket.print_tickets_in_window())
print(10%1)