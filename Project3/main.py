import random


class PowerBallTicket:

    TICKET_COST = 2

    def __init__(self, numbers=None):
        # sanity checking is good, not required

        if numbers: # if numbers != None
            if len(numbers) != 6:
                raise ValueError
            self._white_numbers = numbers[:5]
            self._red_number = numbers[5]

            # todo check for valid range
        else:
            self._white_numbers = random.choices(range(1, 70), k=5)
            self._red_number = random.randint(1, 26)

        self._white_numbers.sort()

    def get_winnings(self, winning_ticket):
        white_matches = 0
        red_matches = self._red_number == winning_ticket.get_red_number()

        for number in self._white_numbers:
            if number in winning_ticket.get_white_numbers():
                white_matches += 1

        if white_matches == 5 and red_matches:
            return 2_000_000_000
        elif white_matches == 5:
            return 1_000_000
        elif white_matches == 4 and red_matches:
            return 50_000
        elif white_matches == 4 or ( white_matches == 3 and red_matches ):
            return 100
        elif white_matches == 3 or ( white_matches == 2 and red_matches ):
            return 7
        elif red_matches:
            return 4
        else:
            return 0

    def get_white_numbers(self):
        # safer to give a copy
        return self._white_numbers[:]

    def get_red_number(self):
        return self._red_number

    def __str__(self):
        return " ".join(str(number) for number in self._white_numbers) + " PowerBall: " + str(self._red_number)

# ticket1 = PowerBallTicket([1,2,3,4,5,6])
# ticket2 = PowerBallTicket([5,4,3,2,1,7])
#
# print(f"{ticket2.get_winnings(ticket1):,}")



play_again = 'y'
total_spent = 0
total_won = 0

while play_again == 'y':
    winning_ticket = PowerBallTicket()
    ticket_type = input("Do you want to pick numbers or get random tickets (p/r)").lower()
    if ticket_type == 'p':
        numbers = []
        for number in range(5):
            number = 0
            while number <= 0 or number >= 70 or number in numbers:
                number = int(input(f"Enter a number 1-69 for number {len(numbers)+1}"))
            numbers.append(number)
        number = 0
        while number <= 0 or number >= 27:
            number = int(input("Enter a number 1-26 for the powerball"))
        numbers.append(number)
        ticket = PowerBallTicket(numbers)
        print(f"Winning Ticket: {winning_ticket}")
        print(f"You won ${ticket.get_winnings(winning_ticket)}")
        total_won += ticket.get_winnings(winning_ticket)
        total_spent += PowerBallTicket.TICKET_COST

    else:
        number_of_tickets = int(input("How many random tickets do you want?"))
        print(f"Winning Ticket: {winning_ticket}")
        for ticket in range(number_of_tickets):
            ticket = PowerBallTicket()
            if ticket.get_winnings(winning_ticket) > 100:
                print(f"{ticket} wins ${ticket.get_winnings(winning_ticket)}")
            total_won += ticket.get_winnings(winning_ticket)
            total_spent += PowerBallTicket.TICKET_COST

    print(f"total spent: ${total_spent} - total won: ${total_won} - net loss: ${total_spent-total_won}")

    play_again = input("Do you want to play powerball again? y/n").lower()