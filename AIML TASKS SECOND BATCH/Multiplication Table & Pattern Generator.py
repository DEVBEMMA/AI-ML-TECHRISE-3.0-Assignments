"""
Exercise 6 — Multiplication Table & Pattern Generator
Topics: Functions · Nested Loops · If statements

Write a function print_pattern_table(n) that:
- Prints multiplication tables from 1 to n.
- Uses nested loops.
- Highlights (with *) all multiples of 3, 5, and 7 using if conditions.
- Also prints a visual pattern (e.g., triangle or square) based on n.

In main code, generate patterns for n = 10 and n = 15.
"""


# Function to print a multiplication table
def print_multiplication_table(size):
    # Loop through each row from 1 up to 'size'
    for row in range(1, size + 1):
# Loop through each column from 1 up to 'size'
        for col in range(1, size + 1):
            # Multiply row and column to get the product
            product = row * col
            # Check if product is divisible by 3, 5, or 7
            if product % 3 == 0 or product % 5 == 0 or product % 7 == 0:
                # If divisible, print product with a star (*) beside it
                # end="\t" means stay on the same line and add a tab space
                print(f"{product}*", end="\t")
            else:
                # If not divisible, just print the product normally
                print(product, end="\t")
        # After finishing one row, move to the next line
        print()


# Function to print a number triangle pattern
def print_number_pattern(rows):
    # Loop through each row from 1 up to 'rows'
    for row in range(1, rows + 1):
        # Loop through numbers from 1 up to the current row number
        for col in range(1, row + 1):
            # Print the column number on the same line with a space
            print(col, end=" ")
        # After finishing one row, move to the next line
        print()


# Main function to run both tasks
def main():
    # Print heading for multiplication table
    print(" Multiplication Table (with * for multiples of 3, 5, or 7)")
    # Call the multiplication table function with size 10
    print_multiplication_table(10)

    # Print heading for number triangle pattern
    # \n adds a blank line before the heading
    print("\n Number Triangle Pattern ")
    # Call the number pattern function with 5 rows
    print_number_pattern(5)


# Run the main function so the program executes
main()
