#!/usr/bin/env python3
# Activity7
# Vahini Madipalli
# Course: ISQA3900-850: Web Application Development
# Date: 11-12-2020
# creating class objects and defining methods

class Customer:
    # initializing attributes
    def __init__(self, custumer_num="", fname="", lname="", company="", street="", city="", state="", zipcode=00000):
        self.cust_number = custumer_num       # attribute 1
        self.fname = fname              # attribute 2
        self.lname = lname              # attribute 3
        self.company = company          # attribute 4
        self.street = street            # attribute 5
        self.city = city                # attribute 6
        self.state = state              # attribute 7
        self.zipcode = zipcode          # attribute 8

    def cust_num(self):
        return self.cust_number

    def cust_name(self):
        return self.fname + " " + self.lname


    def cust_fullAddress(self):
        # when company attribute is empty
        if self.company == "":
           return '\n' + self.street + '\n' + self.city + ', ' + self.state + ' ' + str(self.zipcode)
        # when company attribute is not empty
        else:
            return '\n' + self.company + ' ' + '\n' + self.street + '\n' + self.city + ', ' + self.state + ' ' + str(self.zipcode)

    def company_name(self):
        return self.company


    # initializing str to display as required
    def __str__(self):
        return '{0}{1}'.format(Customer.cust_name(self), Customer.cust_fullAddress(self))
