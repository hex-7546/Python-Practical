a = int(input("Enter 1st no: "))
b = int(input("Enter 2nd no: "))
c = int(input("Enter 3rd no: "))

def quad_eqn(a, b, c):
    D = b**2 - 4*a*c
    if D > 0:
        print("Roots are real and distinct")
    elif D == 0:
        print("Roots are real and equal")
    elif D < 0:
        print("No real roots")
    else:
        print("try again")

quad_eqn(a, b, c)