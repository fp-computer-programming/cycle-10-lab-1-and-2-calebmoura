# Author: Caleb Moura

# Set sum to 0.
total_sum = 0

# Start the loop.
while True:
    # Prompt user to input number.
    user_input = input("Enter a number (or -1 to end): ")

    # Convert input to integer.
    number = int(user_input)

    # Check if user wants to end program.
    if number == -1:
        # Break out of the loop if input is -1.
        break

    # Add entered number to total sum.
    total_sum += number

# Display sum of all numbers input by user.
print(f"The sum of the numbers entered is: {total_sum}")