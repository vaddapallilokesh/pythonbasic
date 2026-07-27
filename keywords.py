import keyword

# 1. Print total number of keywords and the full list
print("Total keywords:", len(keyword.kwlist))
print("Keywords list:", keyword.kwlist)

'''Total keywords: 35
Keywords list: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']'''


# 2. Check if a user-input word is a keyword
word = input("Enter a word: ")
if keyword.iskeyword(word):

    print(f"'{word}' is a Python keyword.")
else:
    
    print(f"'{word}' is NOT a Python keyword.")
'''Enter a word: else
'else' is a Python keyword.'''
    

# 3. Trying to use keywords as variable names (will cause errors)
# Uncomment these lines to see the errors:
# for = 5      # SyntaxError: invalid syntax
# True = 10    # SyntaxError: cannot assign to True

# Challenge — print soft keywords separately
print("Soft keywords:", keyword.softkwlist)
print("Hard keywords:", [kw for kw in keyword.kwlist if kw not in keyword.softkwlist])

'''Soft keywords: ['_', 'case', 'match', 'type']
Hard keywords: ['False', 'None', 'True', 'and',
'as', 'assert', 'async', 'await', 'break', 'class',
'continue', 'def', 'del', 'elif', 'else', 'except',
'finally', 'for', 'from', 'global', 'if', 'import',
'in', 'is', 'lambda', 'nonlocal',
'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']'''
