import json
import math

a = float(input("enter coefficient a: "))
b = float(input("enter coefficient b: "))
c = float(input("enter coefficient c: "))

D = b**2 - 4*a*c
print(f"discriminant (D) = {D}")

if D > 0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print(f"The two roots are {root1} and {root2}")
elif D == 0: 
    root = (-b) / (2*a)
    print(f"The only root is {root}")
else:
    print("There is no solution")
