#!/usr/bin/python3
"""Defines the class MyList that extends list"""

class MyList(list):
    """MyList class inherites from list and has has print_sorted which returns a sorted list"""

    def print_sorted(self):
        """returns the list in ascending sorted order"""
        print(sorted(self))
    

    

