import math
def circle_status(radius):
    area =  round(math.pi * (radius ** 2), 2) # precision 2 
    circumference = round((math.pi * radius * 2), 2) # precision 2 
    return area, circumference
    

a, c =  (circle_status(5))
print("Area:", a, "Circumference:", c)