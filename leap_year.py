#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Oct. 31, 2023
# This program gets a year from the user and will tell them if it is a leap year or not. It involves the use of mods as well.


def main():
    # introduce program to user
    print(
        "This program gets a year from the user and will tell them if it is a leap year or not. It involves the use of mods as well.\n"
    )

    # declare variable and get user input
    year_str = input("Please enter a year: ")

    # try converting string to integer
    try:
        year_int = int(year_str)
        if year_int % 4 == 0:
            if year_int % 100 == 0:
                if year_int % 400 == 0:
                    print("{} is a leap year.".format(year_int))
                else:
                    print("{} is not a leap year.".format(year_int))
            else:
                print("{} is a leap year.".format(year_int))
        else:
            print("{} is not a leap year.".format(year_int))

    # catch if user input isn't valid
    except Exception:
        print("{} is not a valid input.".format(year_str))


if __name__ == "__main__":
    main()
