a=int(input("enter the number of rows"))
b=float(input("enter the starting number"))
if(a<0):
      print("please enter the positive number")
else:
    for i in range(1,a+1):
       for j in range(1,i):
           print("%.if"%b,end=" ")
           b=b+0.1
       print(" ")
         
