# Written by Vincent Diep starting 09/27/2023

import random

# define max lines of slot machine
MAX_LINES = 3
# define max bet
MAX_BET = 10000
# define min bet
MIN_BET = 1

# define rows
ROWS = 3
# define columns
COLS = 3

symbol_count = {
    "X": 3,
    "O": 6,
    "S": 9,
    "W": 12
}

symbol_value = {
    "X": 5,
    "O": 3,
    "S": 2,
    "W": 1.5
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        # check if symbols in the line are the same
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    # populate symbols into a list
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    # generate columns
    for _ in range(cols):
        column = []
        # create a copy of symbols
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    # transpose columns into rows
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i < len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        # moves to next line after row is printed
        print()

def deposit():
    while True:
        # prompt user
        amount = input("How much would you like to deposit? $")
        # check if input is a number
        if amount.isdigit():
            # convert number to integer
            amount = int(amount)
            # check for negatives or zero
            if amount > 0:
                # print("You now have $" + str(amount))
                break
            else:
                print("Amount must be greater than 0.")
        # if input is not number, prompt for number
        else:
            print("Please enter a number greater than 0.")

    return amount
    
def get_number_of_lines():
    while True:
        # prompt user
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        # check if input is a number
        if lines.isdigit():
            # convert number to integer
            lines = int(lines)
            # check for negatives or zero
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        # if input is not number, prompt for number
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        # prompt user
        amount = input("How much would you like to bet on each line? $")
        # check if input is a number
        if amount.isdigit():
            # convert number to integer
            amount = int(amount)
            # check for negatives or zero
            if MIN_BET <= amount <= MAX_BET:
                # print("You placed a bet of $" + str(amount))
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}.")
        # if input is not number, prompt for number
        else:
            print("Please enter a number.")

    return amount

def spin(balance):
    lines = get_number_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Bet amount exceeds current balance of: ${balance}")
        else: 
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines: ", *winning_lines)

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play. (q to quit)")
        if answer == "q":
            break
        # update balance
        balance += spin(balance)

    print(f"You left with ${balance}")


main() 