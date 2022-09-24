"""CP1404 Score with menu program"""

MENU = """(G)et score
(D)isplay result
(P)rint stars
(Q)uit"""


def main():
    """Results program with menu"""
    score = 0
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "D":
            grade = grade_score(score)
            print(f"Result: {grade}")
        elif choice == "P":
            print_characters(int(score))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>>").upper()


def get_valid_score():
    """Get a valid score"""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def print_characters(length):
    """Print a line of * for length n"""
    print(length * "*")


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