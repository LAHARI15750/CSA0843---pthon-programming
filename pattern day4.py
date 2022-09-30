n=int(input("enter the number of rows"))
for row in range(1,n):
    for column in range(row,0,-1):
        print(column,end=' ')
    print("")   
