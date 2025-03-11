# Lorraine Byrne
# CS 361
# Microservice A for Abraham's Main Event App Project
# References
# https://pypi.org/project/holidays/
# https://www.geeksforgeeks.org/python-holidays-library/
# https://stackoverflow.com/questions/70391399/datetime-datatime-strptimedate-y-m-d-adds-000000-for-different-dates
# https://www.geeksforgeeks.org/python-append-to-a-file/

import time
import holidays
import datetime

# defines which country you are going to use for the holidays package
us_holidays = holidays.US()

if __name__ == '__main__':
    time.sleep(1)
    # place to store all the dates as a list
    added_dates = []

    # opens the personal calendar to check the date
    # sees if the date is in the right format
    # if not, an error text will pop up
    while True:

        with open("personal-calendar.txt", "r") as file:
            dates = file.readlines()
        # Checks all lines in the calendar for dates
        # opens the holiday text file as append, to add new dates
            with open("holiday-note.txt", "a") as file:
                for line in dates:
                    line = line.strip()
                    if line not in added_dates:
                        try:
                            event_date = datetime.datetime.strptime(
                                line, "%Y-%m-%d").date()

                            # If event is in the holiday package,
                            # then write "Yes" in holiday-note.txt w/ holiday
                            # then write "no" into holiday-note.txt w/ holiday
                            # adds the dates to the previously checked dates
                            # checks every 30 seconds
                            if event_date in us_holidays:
                                print(
                                    f"{event_date} is a holiday: {us_holidays[event_date]}")
                                result = print(
                                    f"{event_date} is a holiday: {us_holidays[event_date]}")
                                added_dates.append(result)

                            else:
                                print(f"{event_date} is not a holiday")
                                result = f"{event_date} is not a holiday"
                                added_dates.append(result)
                        except ValueError:
                            print(
                                "Invalid date format in file. Expected YYYY-MM-DD.")
            # cycle every 30 seconds
            time.sleep(30)
