items = {"Pen": 10, "Book": 50, "Bag": 200, "Pencil": 5}
sorted_items = sorted(items.items(), key=lambda x: x[1])

print("Items sorted by price:")
for name, price in sorted_items:
    print(name, ":", price)

'''output-Items sorted by price:
Pencil : 5
Pen : 10
Book : 50
Bag : 200
'''
