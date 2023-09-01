age=int(input("enter the age"))
re=age>=18
out="can vote"*re + "cannt vote"*(1-re)
print(out)
