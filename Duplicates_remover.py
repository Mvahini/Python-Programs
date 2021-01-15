#!/usr/bin/env python3
# Activity4
# Vahini Madipalli
# Course: ISQA3900-850: Web Application Development
# Date: 09-27-2020
# Creating a python program to remove the duplicates in a list and sorting the list

names = \
    ["maria", "maria", "will", "sam", "maria", "kahn", "sam", "barry", "george", "hank", "belinda", "maria", "karthik"]


# Defining function to remove the duplicates from a list
def duplicates_remove(names):
    a = []
    for i in names:
        if i not in a:
            a.append(i)
    return a


# Assign removed duplicate list to a variable
result = duplicates_remove(names)

# Sort original list and duplicate removed list
result.sort()
names.sort()

# Print values
print("Initial List of Names:\n" + str(names))
print("List of Unique Names:\n" + str(result))
