x=[[1,2],
  [5,3]]
y=[[2,3],
   [4,1]]
result=[[0,0],[0,0]]
for i in range(len(x)):
    for j in range(len(x)):
        result[i][j]=x[i][j]+y[i][j]
        
for r in result:
    print(r)
