#!/usr/bin/env python3
# Activity4
# Vahini Madipalli
# Course: ISQA3900-850: Web Application Development
# Date: 09-27-2020
# Creating python program which inputs scores and print sum,avg and letter grade.

# Initialize variables
counter = 0
score_total = 0
test_score = 0
# initialize a list
score_list = []


# Define function to get letter grade based on the average score
def get_letterGrade(average_score):
    if average_score <= 59.40:
        return "F"
    if 59.5 <= average_score <= - 72.49:
        return "D"
    if 72.5 <= average_score <= 77.49:
        return "C"
    if 77.5 <= average_score <= 82.49:
        return "C+"
    if 82.5 <= average_score <= 88.49:
        return "B"
    if 88.5 <= average_score <= 92.49:
        return "B+"
    elif 92.5 <= average_score <= 100:
        return "A"


# Infinite loop to execute loop body while expression evaluates to TRUE
while True:

    # Handling exceptions using TRY
    try:
        test_score = input("Enter test score (or '-1' to quit): ")

        if test_score != "-1":
            test_score = int(test_score)
            if test_score >= 0 and test_score <= 100:
                counter += 1
        else:

            # Below is the validation code for divide by zero issue
            if counter == 0:
                print("Please enter at least one score")
            else:
                break

        if counter > 0:
            if test_score >= 0 and test_score <= 100:
                score_list.append(test_score)  # Adding scores to the list
                score_total += test_score

            else:
                print("You must enter integer values >= 0 and <= 100 or -1 to quit. Try again.")

        else:
            continue

    # Catching exception here from TRY block
    except ValueError:
        print("You must enter integer values >= 0 and <= 100 or -1 to quit. Try again.")


if counter > 0 and test_score == "-1":
    # Calculating average score and letter grade based on the avg
    average_score = score_total / counter
    letter_grade = get_letterGrade(average_score)

    # Print total,avg and letter grade
    print("\nScores:   ", score_list)
    print("Total:    ", score_total)
    print("Average Score:   ", average_score)
    print("Letter Grade:    ", letter_grade)




