# Program with inconsistent indentation
'''x = 5
if x > 0:
    print("Positive")
  print("This line is misaligned")  # <- Wrong indentation
else:
    print("Non-positive")

syntax error - unident does not match outer indentation level'''

x = 5
if x > 0:
    print("Positive")
    print("This line is aligned correctly")
else:
    print("Non-positive")

'''output -
Positive
This line is aligned correctly '''

