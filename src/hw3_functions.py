"""
HW 3: Lists and Arrays
Josh Reginaldo -- https://github.com/itmd-413-jreginaldo/Lists-and-Arrays

Program Description: This program will execute matrix multiplication
and calculate the final cost of items entered in by the user
"""


def check_for_negative(user_input):
    while user_input < 0:
        try:
            user_input = float(input("Enter price of item> "))

            if user_input < 0:
                print("Negative value detected, positive values only.")

        except ValueError:
            print("\nUnknown value(s) detected, numeric values only.")

    return user_input


def calculate_costs(list_of_prices):
    prices_subtotal = 0

    # Print prices inputted by the user
    # Apply +1 shift to iterator in print to adjust for 0 index

    for x in range(len(list_of_prices)):
        print(f"Item {x + 1}: ${list_of_prices[x]}")
        prices_subtotal += list_of_prices[x]  # Total prices for subtotal

    print(f"Subtotal: ${prices_subtotal:.2f}")
    print(f"7% Item Tax: ${prices_subtotal * .07:.2f}")
    print(f"Final Total: ${prices_subtotal + (prices_subtotal * .07):.2f}")