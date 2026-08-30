
#1. List of 10 integers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("List:", numbers)
print("Length:", len(numbers))

#output-List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Length: 10



#2. List with multiple data types

mixed = [10, 3.14, "Hello", True, [1, 2, 3]]
for element in mixed:
    print(element, "->", type(element))

'''output-
10 -> <class 'int'>
3.14 -> <class 'float'>
Hello -> <class 'str'>
True -> <class 'bool'>
[1, 2, 3] -> <class 'list'> '''   

    
#3. Empty list + append

my_list = []
my_list.append(5)
my_list.append("Python")
my_list.append(3.5)
my_list.append(False)
my_list.append([1,2])
print("Final List:", my_list)

#output-Final List: [5, 'Python', 3.5, False, [1, 2]]


