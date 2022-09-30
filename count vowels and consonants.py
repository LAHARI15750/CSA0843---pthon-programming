str=input("Please enter a string as you wish: ");
l=[]
m=[]
vowels=0
consonants=0
for i in str:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or
       i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
           vowels=vowels+1;
           l.append(i)
    else:
        consonants=consonants+1;
        m.append(i)

print("  The number of vowels:",vowels);
print("vowels are:",l)
print("\nThe number of consonant:",consonants);
print("consonants are:",m)
