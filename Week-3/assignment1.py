#write a program that solvees a quadratic equation
#using a for loop draw a diamond,a triangle , pascals triangle
import cmath


a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))

Answer = ((-b + pow((pow(b,2 )- 4*a*c),0.5))/2*a)
Answer1 = ((-b - pow((pow(b,2 )- 4*a*c),0.5))/2*a)
print ("The answers to the equation are either {} or {}.".format(Answer,Answer1))