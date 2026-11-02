percentage = float(input("Enter your percentage: "))
attendance = float(input("Enter your attendance: "))

eligible = (percentage > 75) and (attendance > 90)

print("Eligible for scholarship:", eligible)

'''Enter your percentage: 80.96
Enter your attendance: 93.76
Eligible for scholarship: True'''


