p=int(input("enter the principal"))
t=int(input("enter the time"))
print("is customer is senior citizen(y/n)")
c=input("enter y or n")
if p<0:
    break
if c=='y':
    r=12
if c=='n':
    r=10
si=p*t*r/100
print(si)
    
