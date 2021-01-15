#!/usr/bin/env python3
# Activity7
# Vahini Madipalli
# Course: ISQA3900-850: Web Application Development
# Date: 11-12-2020
# Creating python program which reads from the csv files, display the list, search based on cust_id

from Customer import Customer
import csv


FILENAME = "customers.csv"
customer_details = []

def read_csv():

   # Exception handling to handle invalid values and read from csv
   try:
    with open(FILENAME, newline="") as file:
        read = csv.reader(file)
        next(read)
        for row in read:
            customer_details.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]])
    return customer_details

   # file not found exception handler
   except OSError:
      print("File cannot be opened or read" + FILENAME)


# function to read customer list
def read_customerlist():
    for data in customer_details:
        customer_id_name = Customer(data[0],data[1],data[2])
        print('{0} : {1}'.format(customer_id_name.cust_num(),customer_id_name.cust_name()))
        #print(str(customer_id_name.cust_num()))

# function to search based on customer_id
def search_id(customer_id):

    for data in customer_details:
        customer_id_name = Customer(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7])
        if(customer_id == customer_id_name.cust_num()):
             return customer_id_name
             break
    return None


def main():
    customer_details = read_csv()
    print("CUSTOMER VIEWER")
    print()
    print("ALL CUSTOMERS")
    print("----------------------------")
    read_customerlist()
    print()
    choice = "y"

    # repetitive structure to prompt and look up
    while choice.lower() == "y":

        try:
            customer_id = input("Enter Customer Id: ")
            customer_object = search_id(customer_id)
            if(customer_object == None):
                print()
                print("Customer a does not exist")
                print()
            else:
                print()
                print(customer_object)
                print()

            choice = input("Would you like to continue? y/n: ")
            print()

        # exception to handle invalid customer id entries
        except ValueError:
             print("Customer a does not exist")

             choice = input("Would you like to continue? y/n: ")
             print()

    print("Bye!")



if __name__ == "__main__":
    main()