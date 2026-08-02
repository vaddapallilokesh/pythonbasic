first = "Lokesh"
last = "Vaddapalli"
full_name = first + " " + last


print(full_name.upper())      
print(full_name.lower())    
print(full_name.title())      
print(len(full_name))         
print(full_name[0], full_name[-1])  


first_name = full_name[:full_name.find(" ")]
print(first_name)

'''output-
LOKESH VADDAPALLI
lokesh vaddapalli
Lokesh Vaddapalli
17
L i
Lokesh'''

