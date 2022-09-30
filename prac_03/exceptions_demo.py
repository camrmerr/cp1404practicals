"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? If an input other than an int is entered
2. When will a ZeroDivisionError occur? Whenever a denominator of 0 is entered
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Use a while loop to
address denominator's of zero before the code tries to perform the calculation
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")