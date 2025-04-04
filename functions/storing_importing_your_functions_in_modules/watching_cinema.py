import printing_tickets

unprinted_tickets = ['first class', 'business class', 'economy class']
completed_tickets = []

printing_tickets.print_tickets(unprinted_tickets, completed_tickets)
printing_tickets.show_completed_tickets(completed_tickets)
# Compare this snippet from pizza.py: