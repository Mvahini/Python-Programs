#!/usr/bin/env python3
# Activity5
# Vahini Madipalli
# Course: ISQA3900-850: Web Application Development
# Date: 10-25-2020
# Creating python program which reads and writes the csv files

import csv

# display a welcome message
print("The Miles Per Gallon program")
print()


# Initiating the list
final_mpg_list = []
FILENAME = "trips.csv"


# Function to prompt user to enter miles
def get_miles(prompt):
    while True:
        try:
            miles_driven = int(input(prompt))
            return miles_driven
        except ValueError:
            print("Enter numeric values only. Try again.")
            continue


# Function to prompt user to enter gallons used
def get_gallons(prompt):
    while True:
        try:
            gallons_used = int(input(prompt))
            return gallons_used
        except ValueError:
            print("Enter numeric values only. Try again.")
            continue


# Append to list and write/read to/from csv
def get_mpglist(miles_driven, gallons_used, mpg, count):

    mpg_list = []
    mpg_list.append(count)
    mpg_list.append(miles_driven)
    mpg_list.append(gallons_used)
    mpg_list.append(mpg)
    final_mpg_list.append(mpg_list)
    write_mpg(final_mpg_list)
    read_mpg()


# write function to write values to csv
def write_mpg(final_mpg_list):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(final_mpg_list)

        # for row in reader:
        # read.append(row)
    # return read


# read function to read values to csv
def read_mpg():

   # Exception handling to handle invalid values
   try:
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(str(row[0]) + "." +  "Miles: " + str(row[1]) + "  " + " Gallons of Gas: " + str(row[2]) + "  " + " Mpg: " + str(row[3]))
   except FileNotFoundError:
       print("File not found:" + FILENAME)

def new_trip():

    count = 0

    while True:
        choice_trip = input("Would you like to enter trip data? y/n: ")

        if (choice_trip.lower() == "y"):

            # Call functions and assign values to variables
            miles_driven = get_miles("Enter miles driven: \t")
            gallons_used = get_gallons("Enter gallons of gas used:\t")

            # calculate and round miles per gallon

            mpg = miles_driven / gallons_used
            mpg = round(mpg, 2)

            count = count + 1

            # Function call for list
            get_mpglist(miles_driven, gallons_used, mpg, count)


        else:
            print("Trips saved to file: trips.csv")
            break


def main():
    choice = (input("Would you like to read trips from a file? y/n: "))
    if (choice.lower() == "y"):
        read_mpg()
        choice = "n"

        new_trip()

    if (choice.lower() == "n"):

        new_trip()




if __name__ == "__main__":
    main()