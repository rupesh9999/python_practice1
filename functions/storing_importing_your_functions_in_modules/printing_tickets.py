def print_tickets(unprinted_tickets, completed_tickets):
    """
    Simulate printing each ticket, until none are left.
    Move each ticket to completed_tickets after printing.
    """
    while unprinted_tickets:
        current_ticket = unprinted_tickets.pop()
        print(f"Printing ticket: {current_ticket}")
        completed_tickets.append(current_ticket)

def show_completed_tickets(completed_tickets):
    """Show all the tickets that were printed."""
    print("\nThe following tickets have been printed:")
    for completed_ticket in completed_tickets:
        print(completed_ticket)