# Function to sum numbers in a list
def sum_numbers(numbers):
    return sum(numbers)

# Print even numbers between 1 and 20 using a loop
def print_even_numbers():
    print("Even numbers between 1 and 20:")
    for i in range(1, 21):
        if i % 2 == 0:
            print(i, end=" ")
    print()  # Newline after printing

# Program to find the largest number in a list
def find_largest_number(numbers):
    if not numbers:  # Handle empty list case
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
