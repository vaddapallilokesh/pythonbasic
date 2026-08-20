text = input("Enter a string: ")
vowels = consonants = digits = spaces = 0

for ch in text:
    if ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    elif ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)


'''output-
Enter a string: srihari26
Vowels: 3
Consonants: 4
Digits: 2
Spaces: 0
'''
