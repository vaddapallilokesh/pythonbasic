#Task 5: Temperature Converter

def celsius_to_fahrenheit(c):
    return (c*9/5)+32

def fahrenheit_to_celsius(f):
    return (f-32)*(5/9)

print("25C =", celsius_to_fahrenheit(25), "F")
print("77F =", fahrenheit_to_celsius(77), "C")

#output-
#25C = 77.0 F
#77F = 25.0 C

