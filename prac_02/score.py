"""
CP1404/CP5632 - Practical
Program to determine score status
"""
from random import randint


def main():
    score = float(input("Enter score: "))
    grade = grade_score(score)
    print(f"Result: {grade}")
    random_score = randint(0, 100)
    grade = grade_score(random_score)
    print(f"Result: {grade}")


def grade_score(score):
    """Convert score to grade"""
    if score < 0 or score > 100:
        result = "Invalid Score"
    elif score < 50:
        result = "Bad"
    elif score < 90:
        result = "Passable"
    else:
        result = "Excellent"
    return result


main()