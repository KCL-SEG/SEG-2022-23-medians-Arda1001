"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
from statistics import median


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

print(numbers)

result = median(numbers)
print(result)

# Doing it without median package.
# numbers.sort()

# if (len(numbers) % 2 == 1):
#     median_index = (len(numbers) + 1) / 2
#     result = numbers[int(median_index - 1)]  

# else:
#     median_index = len(numbers) / 2
#     result = (numbers[int(median_index)] + numbers[int(median_index) - 1]) / 2

# print(result)