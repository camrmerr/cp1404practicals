"""
"Quick Pick" Lottery Ticket Generator
Program to generate a number of "Quick Picks" requested by user
"Quick Picks" consist of 6 random numbers between 1 and 45
"""

from random import randrange

RANGE_START = 1  # Min value for number in line
RANGE_END = 45  # Max value for number in line
LENGTH_OF_PICK = 6  # Number of numbers to generate per line


def main():
    """Quick Pick generator"""
    number_of_picks = get_valid_number("How many quick picks? ")
    quick_picks = generate_quick_picks(number_of_picks)
    display_quick_picks(quick_picks)


def get_valid_number(prompt):
    """Get valid number from user"""
    valid_value = False
    while not valid_value:
        try:
            value = int(input(prompt))
            if value > 0:  # Error check to ensure valid number of quick picks
                valid_value = True
            else:
                print("Number of quick picks must be more than 0")
        except ValueError:  # Error check to ensure integer is entered
            print("Please enter a valid number")
    return value


def generate_quick_picks(number_of_picks):
    quick_picks = []
    for i in range(number_of_picks):
        pick = []
        for j in range(LENGTH_OF_PICK):
            number = randrange(RANGE_START, (RANGE_END + 1))  # To ensure RANGE_END is inclusive
            while number in pick:  # Ensure numbers are not duplicated
                number = randrange(RANGE_START, (RANGE_END + 1))
            pick.append(number)
        quick_picks.append(pick)
    return quick_picks


def display_quick_picks(quick_picks):
    """Display data in sorted, formatted grid"""
    for pick in quick_picks:
        pick.sort()
        for number in pick:
            print(f"{number:2}", end=" ")
        print()


main()
