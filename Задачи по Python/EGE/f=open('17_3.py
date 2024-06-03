f=open('17_3.txt','r')
F=[int(i) for i in range(f)]
a=[]
chislo=0
for i in range(len(F)):
    if F[i]%117==min(F) or F[i+1]%117==min(F):
        chislo+=1
        a.append(F[i]+F[i+1])
print(chislo)
print(max(a))



4
f=open('17_3.txt','r')
F=[int(i) for i in range(f)]
a=[]
for i in range(len(F)):
    if F[i]%17==0:
        a.append(F[i])
mi=min(a)
c=[]
chislo=0
for i in range(len(F)):   
    if F[i]%mi==0 or F[i+1]%mi==0:
        chislo+=1
        c.append(F[i]+F[i+1])
print(chislo)
print(max(c))