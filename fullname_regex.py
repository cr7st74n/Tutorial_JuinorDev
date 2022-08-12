"""Cristian Gonzalez, 4/2/2022.This program will allow us to verify if
 you write a valid Full Name"""
import re

def main():
    try:
        Full_name = Input()
        result = Process(Full_name)
    except KeyError:
        print("Error")


def Input():
    Full_name = input("Enter your full name: first middle last. ")
    return Full_name


def Process(Full_name):
    name_regex = re.compile(r"\D+\s\D+(\s)?(\D+)?")  # Used some Expressions to match a Common name that could have any characters, but no digits.
    source = name_regex.search(Full_name)

    while source is None :
        Full_name = input("This doesn't look like a name ")
        source = name_regex.search(Full_name)
    else:
        print("Here is the name: ",source.group())


main()