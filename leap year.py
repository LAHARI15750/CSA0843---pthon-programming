n=float(input("enter the year"))
if(n==0):
    print("entered year is not valid")
elif(n%4==0):
    print("Given year is a leap year")
else:
    print("Given year is non leap year")
