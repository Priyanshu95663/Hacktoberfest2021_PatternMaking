
t=input("Dimensions of design")
s=list(map(int,(t.split(" "))))
a=s[0]
b=s[1]
z=list()
for i in range(0,a):
    if i%2!=0:
        z.append(i)
e=int((a-1)/2)
c=int(b)    
for i in range(0,e):
    print("-"*int((c-3)/2)+".|."*int(z[i])+"-"*int((c-3)/2))
    c-=6
print("-"*int((b-7)/2)+"WELCOME"+"-"*int((b-7)/2))

for i in range(e-1,-1,-1):
    print("-"*int((c+3)/2)+".|."*int(z[i])+"-"*int((c+3)/2))
    c+=6
