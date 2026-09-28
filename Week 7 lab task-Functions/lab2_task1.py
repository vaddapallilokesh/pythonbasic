#Task 1: Positional and Keyword Arguments

def student_info(name, roll_no, branch):
    print("Name:", name)
    print("Roll No:", roll_no)
    print("Branch:", branch)

# Positional arguments
student_info("Lokesh", 100, "CSE")

# Keyword arguments 
student_info(branch="CSE", roll_no=100, name="Lokesh")


'''output-
Name: Lokesh
Roll No: 100
Branch: CSE
Name: Lokesh
Roll No: 100
Branch: CSE
'''
