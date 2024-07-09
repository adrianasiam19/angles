#Quwstion 13
import math

def findC(alpha, beta, A):
    #Calculate gamma
    gamma = 180 - alpha - beta
    #Angles converted to radians
    sin_gamma = math.sin(math.radians(gamma))
    #Calculate length of C
    C = A * sin_gamma / math.sin(math.radians(alpha))
    print(f"The angle gamma is: {gamma} degrees")
    print("Length of side C is:", C)

#Declare the valid user input for all while conditions
while True:
    alpha = int(input("Enter the value of angle alpha in degrees: "))
    if alpha < 0:
        print("Invalid input, enter an positive angle")
    else:
        break

while True:
    beta = int(input("Enter the value of angle beta in degrees: "))
    if beta < 0:
        print("Invalid input, enter an positive angle")
    elif beta + alpha > 180:
        print("Sum of angles cannot exceed 180")
    else:
        break

while True:
    A = int(input("Enter the length of side A: "))
    if A < 0:
        print("Invalid input, enter an positive angle")
    else:
        break

findC(alpha, beta, A)