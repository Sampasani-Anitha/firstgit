print("CALCULATING THE AREA :: \n")
print("\n1.square\n 2.triangle \n 3.rectangle \n 4.circle\n")
print("choose the option from the above beween 1 to 4 ! :\n")
choice=int(input("enter your choice"))
if choice==1:
    a=float(input("enter the side of square"))
    area=a**2
    
    print(f"area of the square{area}")

elif choice==2:
    a=float(input("enter the side of rectangle"))
    area=l*a
    print(f"area of the rectagle{area}")
elif choice==3:
    a=float(input("enter the side of triangle"))
    b=float(input("enetr the height value"))
    area=0.5*a*b
    print(f"area of the triangle{area}")

elif choice==4:
    a=float(input("enter the radius of the circle"))
    b=3.14
    area=b*a*2
    print(f"area of the circle{area}")

else:
    print("invalid choice:")
