# Event Microservice
## Is your event on a holiday?

# Communication Contract
## How to REQUEST Data
### Main program writes a date into the personal events text file. Once that date is written (in the correct formate), the Holiday microservice will begin to work to check the event.
### Example call:
### userInput == input("Please enter the date of your event YEAR --- MONTH-- DAY)
### if userInput is valid
### with open(budget.txt, w) as file:
### file.write(userInput)
## How to RECEIVE Data
### Once the microservice runs the date, it will write onto a new holiday.txt Yes\n then stating what holiday it is. The main program then reads this file will display either a balloon or nothing if it falls on a holiday or not, respectively
### Example call:
#### with open (holiday.txt, r) as file
#### if line 1 == Yes
#### create file path to balloon jpeg
#### if line 1 === no
#### no path is created


# UML sequence diagram:
![alt text](image.png)
