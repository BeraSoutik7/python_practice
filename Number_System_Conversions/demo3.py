s1 = bin(10)
s2 = bin(20)
print(s1)
print(s2)
s2 = bin(20)
count=0
for i in range(len(s1)):
    print(s1[i],s2[i])
    if(s1[i]!=s2[i]):
        
        count+=1
print(count)