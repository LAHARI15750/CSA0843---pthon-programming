def count_primes_nums(count1):
    primenumbers(count1=0)
def count_composites_nums(count2):
    compositenumbers(count2=0)
    
n=int(input("enter the range1 n: "))
m=int(input("enter the range2 n: "))
for num in range(n):
    if num<=1:
        continue
    for i in range(2,num):
        if(num%i)==0:
            count2=count2+1
            break
        else:
            count1=count1+1
            
print("number of prime count1",count1)
print("number of composite count2",count2)
            
