from functools import reduce

employees = [
    {"name": "Ravi", "department": "IT", "salary": 50000},
    {"name": "Sita", "department": "HR", "salary": 40000},
    {"name": "Amit", "department": "IT", "salary": 60000},
]

# Filter IT department
it_employees = list(filter(lambda e: e["department"] == "IT", employees))

# Give 10% hike
hiked = list(map(lambda e: {"name": e["name"], "department": e["department"], "salary": int(e["salary"]*1.1)}, it_employees))

# Total salary after hike
total_salary = reduce(lambda a, b: a + b["salary"], hiked, 0)

print("IT Employees after hike:", hiked)
print("Total IT salary expenditure:", total_salary)

'''output-
IT Employees after hike: [{'name': 'Ravi', 'department': 'IT', 'salary': 55000}, {'name': 'Amit', 'department': 'IT', 'salary': 66000}]
Total IT salary expenditure: 121000
'''
