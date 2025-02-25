# Lorraine Byrne
# CS 361
# Microservice A for Abraham's Main Event App Project
# References
# https://www.geeksforgeeks.org/python-pillow-tutorial/#
# https://pypi.org/project/holidays/
# https://www.geeksforgeeks.org/python-holidays-library/
# https://stackoverflow.com/questions/15226898/python-3-2-input-date-function
# https://realpython.com/python-main-function/

import time
import datetime
from PIL import Image

# Has user input a date
# year,month, date and creates a valid format of the date


def input_event():
    year = int(input('Enter a year: '))
    month = int(input('Enter a month: '))
    day = int(input('Enter a day: '))
    return datetime.date(year, month, day)

# Write the date into the personal-calendar text file
# to be stored and read by the microservice


def save_date(date1):
    with open("personal-calendar.txt", "w") as file:
        file.write(date1.strftime("%Y-%m-%d"))

# Reads the new text that the microservice produced
# Lets the user know if their inputted date is a holiday


def is_a_holiday():
    with open("holiday-note.txt", "r") as file:
        print(file.readline())

# Pops up an image if the event is a holiday
# Utilizes similar structure to Assignment 1
# Have to have an image labelled as 1 in your project folder


def holiday_emoji():
    time.sleep(40)
    with open("holiday-note.txt", "r") as file:
        first_line = file.readline().strip()

        if first_line == "Yes":
            path = "C:\\Microservice A\\Images\\1.jpg"
            pic = Image.open(path)
            pic.show()

# main functions
# can easily change functions if need


def main():
    event_date = input_event()
    save_date(event_date)
    is_a_holiday()
    holiday_emoji()


if __name__ == "__main__":
    main()
