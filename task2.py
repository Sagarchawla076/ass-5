# Task 2: Demonstrate List Slicing
# Problem Statement: Write a Python program that:

# 1.   Creates a list of numbers from 1 to 10.
numbers = list(range(1,11))

# 2.   Extracts the first five elements from the list.
first_five = numbers[0:5]

# 3.   Reverses these extracted elements.
reversed_list = first_five[::-1]

# 4.   Prints both the extracted list and the reversed list
print(f"Extracted List: {first_five}")
print(f"Reversed List: {reversed_list}")


