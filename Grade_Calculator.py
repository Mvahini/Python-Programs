#!/usr/bin/env python3
# Activity3
# Vahini Madipalli
# Course: ISQA3900-850: Web Application Development
# Creating python program that takes numeric grade as input and displays letter grade as output.

# define function to display title
def display_title():
    print("Welcome to the Grade Calculator")


# define function to get acceptable value from user
def get_totalPoints():
    total_points = float(input("Enter the total score (0-1000):\t"))
    if total_points < 0 or total_points > 1000:
        print("You must enter integer values >= 0 and <= 1000. Try again.")
        return get_totalPoints()
    else:
        return total_points


# define function to get letter grade based on the average earned
def get_letterGrade(avg):
    if avg < 60:
        return "F"
    if 60 <= avg <= 69.99:
        return "D"
    if 70 <= avg <= 77.99:
        return "C"
    if 78 <= avg <= 81.99:
        return "C+"
    if 82 <= avg <= 87.99:
        return "B"
    elif 88 <= avg <= 91.99:
        return "B+"
    else:
        return "A"


def main():
    display_title()

    # Enter the loop below if the user enter y to continue
    choice = "y"
    while choice.lower() == "y":
        total_points = get_totalPoints()

        # Calculate avg based on total_points from user
        avg = (total_points / 1000) * 100

        letter_grade = get_letterGrade(avg)
        print("Letter grade earned: " + str(letter_grade))

        # Check if user would like to continue
        choice = input("Would you like to enter another score (y/n)? ")
        print()

    print("THE END!!")


if __name__ == '__main__':
    main()
