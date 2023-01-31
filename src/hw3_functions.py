"""
HW 3: Lists and Arrays
Josh Reginaldo -- https://github.com/itmd-413-jreginaldo/Lists-and-Arrays

Program Description: This program will execute matrix multiplication
and calculate the final cost of items entered in by the user
"""
import numpy as np


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


def multiply_matrix(matrix_a, matrix_b):
    final_matrix = []
    while len(final_matrix) < 9:
        for a_row in range(0, 3):  # Loop through each 1x3 list in matrix_a collection
            for y in range(0, 3):
                matrix_b_row_count = 0
                c_row_total = 0
                for x in matrix_a[a_row]:  # Get individual value in 1x3 list in matrix_
                    c_row_total += x * matrix_b[matrix_b_row_count][y]
                    matrix_b_row_count += 1

                final_matrix.append(c_row_total)

    final_matrix = list(np.around(np.array(final_matrix), 2))  # Use numpy to round final list

    print("The multiplication of the matrices is:")
    for row in matrix_a:
        print(row)

    print("\t\tX")

    for row in matrix_b:
        print(row)

    print("\t\t=")

    print(f"{final_matrix[0], final_matrix[1], final_matrix[2]}")
    print(f"{final_matrix[3], final_matrix[4], final_matrix[5]}")
    print(f"{final_matrix[6], final_matrix[7], final_matrix[8]}")
