
#1. Student dictionary

students = {101:"Lokesh",102:"Ravi",103:"Anita",104:"Sara",105:"John"}
print(students)

#output-{101: 'Lokesh', 102: 'Ravi', 103: 'Anita', 104: 'Sara', 105: 'John'}

#2. Add new pairs

students[106] = "Mike"
students[107] = "Emma"
students[108] = "Raj"
print(students)

#output-{101: 'Lokesh', 102: 'Ravi', 103: 'Anita', 104: 'Sara', 105: 'John', 106: 'Mike', 107: 'Emma', 108: 'Raj'}

#3. Update value

print("Before:", students)
students[102] = "Ravi Kumar"
print("After:", students)

'''output-Before: {101: 'Lokesh', 102: 'Ravi', 103: 'Anita', 104: 'Sara',
105: 'John', 106: 'Mike', 107: 'Emma', 108: 'Raj'}
After: {101: 'Lokesh', 102: 'Ravi Kumar', 103: 'Anita', 104: 'Sara', 105: 'John',
106: 'Mike', 107: 'Emma', 108: 'Raj'}'''

#4. From lists using zip

keys = ["a","b","c"]
values = [1,2,3]
d = dict(zip(keys,values))
print(d)

#output- {'a': 1, 'b': 2, 'c': 3}

#5. Nested dictionary

employees = {
    1: {"name":"Alice","department":"HR","salary":50000},
    2: {"name":"Bob","department":"IT","salary":60000},
    3: {"name":"Charlie","department":"Finance","salary":55000}
}
print(employees)



'''
{1: {'name': 'Alice', 'department': 'HR', 'salary': 50000}, 2: {'name': 'Bob', 'department': 'IT',
'salary': 60000}, 3: {'name': 'Charlie', 'department': 'Finance', 'salary': 55000}}'''

