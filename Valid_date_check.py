year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))
day = int(input("Enter day: "))


days_in_month = [31, 28, 31, 30, 31, 30,
                 31, 31, 30, 31, 30, 31]


if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    days_in_month[1] = 29


if 1 <= month <= 12 and 1 <= day <= days_in_month[month - 1]:
    print("Valid Date")
else:
    print("Invalid Date")


    '''output-
Enter year: 2026
Enter month (1-12): 2
Enter day: 31
Invalid Date
'''


