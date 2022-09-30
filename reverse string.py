def reverse(str):
    string="".join(reversed(str))
    return string
s="145*999=144855"
print("the original string is: ",s)
print("the reversed string using reversed() is:",reverse(s))
