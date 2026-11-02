list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2)  
print(list1 is list2)  
print(list1 is list3)   
print(id(list1), id(list2), id(list3))


'''output-
True
False
True
1954254942080 1954254933056 1954254942080
'''
