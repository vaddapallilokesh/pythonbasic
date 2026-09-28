def build_profile(**details):
    print("Profile Card:")
    for key, value in details.items():
        print(f"{key}: {value}")

build_profile(name="Lokesh", age=19, city="Hyderabad", hobby="Reading")
build_profile(name="Amit", department="CSE", year=2)


'''output-
Profile Card:
name: Lokesh
age: 19
city: Hyderabad
hobby: Reading
Profile Card:
name: Amit
department: CSE
year: 2
'''
