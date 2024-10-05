n = 2
ll = 1
r = 2

s = bin(n)
print(s)
l = list(s)

for i in range(ll+1,r+2):
    print(i)
    if(l[i]=='0'):
        l[i]='1'
    else:
        l[i]='0'
print(l)
ans = ''.join(l)
print(int(ans,2))
