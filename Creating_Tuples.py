#1. Tuple of countries

countries = ("India","USA","UK","Canada","Japan","Germany")
print(countries)
print("Type:", type(countries))
print("Length:", len(countries))

'''output-
('India', 'USA', 'UK', 'Canada', 'Japan', 'Germany')
Type: <class 'tuple'>
Length: 6
'''

#2. Single element tuple

single = (10,)   # note the comma
print(single)
print("Type:", type(single))

'''output-
(10,)
Type: <class 'tuple'>
'''


#3. Convert list ↔ tuple

lst = [1,2,3]
tpl = tuple(lst)
print("List to Tuple:", tpl)

tpl2 = (4,5,6)
lst2 = list(tpl2)
print("Tuple to List:", lst2)

'''output-
List to Tuple: (1, 2, 3)
Tuple to List: [4, 5, 6]'''

