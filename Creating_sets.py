#1. Duplicates removed

s = {1,2,2,3,4,4,5,6,7,8}
print(s)
#output- {1, 2, 3, 4, 5, 6, 7, 8}


#2. From list & string

lst = [1,2,3,3,4]
s1 = set(lst)
print("From list:", s1)
s2 = set("hello")
print("From string:", s2)

'''From list: {1, 2, 3, 4}
From string: {'o', 'e', 'l', 'h'}
'''
#3. Add & update

s = {1,2,3}
s.add(4)
s.update([5,6,7])
print(s)

#output{1, 2, 3, 4, 5, 6, 7}
