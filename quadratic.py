import math

def solve_quadratic(a,b,c):
    det=b*b-4*a*c
    if det>0:
        return ((-b + math.sqrt(det))/(2*a), (-b - math.sqrt(det))/(2*a))
    if det==0:
        return (-b + math.sqrt(det))/(2*a)
    else:
        return None
print (solve_quadratic(1,-5,6))
print (solve_quadratic(1,4,4))
print (solve_quadratic(1,0,1))


