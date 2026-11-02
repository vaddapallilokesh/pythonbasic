side1 = int(input(" first side = "))
side2 = int(input(" second side = "))
side3 = int(input(" third side = "))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
            if side1 == side2 == side3:
                print(" Equilateral triangle ")
            elif side1 == side2 or side1 == side3 or side3 == side2:
                print(" Isosceles triangle ")
            else:    
                print(" scalene triangle ")
else:
    print("It is not a valid triangle ")
                
                
            
            
