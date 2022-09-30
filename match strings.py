str=("enter the value: ")
revstr=" "
count=len(str)
while(count>0):
    revstr+=str[count-1]
    count=count-1
print(revstr)
