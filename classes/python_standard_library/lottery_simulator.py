import random

class Lottery:
    """A Class to simulate a lottery draw."""
    
    def __init__(self, draw_size=4):
        """Initialize lottery attributes."""
        self.pool = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
        self.draw_size = draw_size

    def draw_winning_ticket(self):
        """Draw  a winning ticket of random items from the pool."""
        winning_ticket = []
        for _ in range(self.draw_size):
            winning_ticket.append(random.choice(self.pool))
        return winning_ticket

# create a lottery instance
lottery = Lottery()
                          
# players ticket (manually choosen for simplicity)

player_ticket = ['A', 3, 7, 'D']

#draw the winning ticket
winning_ticket = lottery.draw_winning_ticket()

#check matches between player's ticket and winning ticket
matches = sum(1 for p, w in zip(player_ticket, winning_ticket) if p == w)

#print results
print(f"Winning Ticket: {winning_ticket}")
print(f"Your Ticket: {player_ticket}")
print(f"number of matches: {matches}")
if matches == lottery.draw_size:
    print("Congratulations! You have won the lottery!")
else:
    print("Better luck next time!")
