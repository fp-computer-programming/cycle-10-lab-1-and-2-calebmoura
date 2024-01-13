# Author: Caleb Moura

# Define list of numbers.
numbers = [1, 3, 6, 9, 12, 15, 18, 21, 24]

# Iterate through the list using a while loop
index = 0
while index < len(numbers):
    # Check if the current number is not multiple of 3.
    if numbers[index] % 3 != 0:
        # Skip to the next iteration if not multiple of 3.
        index += 1
        continue

    # Print number if it is a multiple of 3.
    print(f"{numbers[index]} is a multiple of 3")

    # Move to next index.
    index += 1