#!/usr/bin/python3
"""Defines the class MyList that extends list"""

class MyList(list):
    """MyList class inherites from list and has has print_sorted which returns a sorted list"""

    def print_sorted(self):
        """returns the list in ascending sorted order"""
        print(sorted(self))
    

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
print("-------------------") 
my_list.print_sorted()
print(my_list)    

