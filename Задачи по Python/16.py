# f=[0]*10**6
# chislo=0
# for n in range(len(f)):
#     if n <2:
#         f[n]=1
#     else:
#         if n>=2 and n%3==0:
#             f[n]=f[n//3]-1
#         if n>=2 and n%3!=0:
#             f[n]=f[n-1]+7
#     if f[n]!=111:
#         chislo+=1
#     else:
#         break
        
# print(chislo)
f=[0]*10**5
chislo=0
for n in range(len(f)):
    if n<4:
        f[n]=n-1
    if n>=4 and n%3==0:
        f[n]=n+2*f[n-1]
    if n>=4 and n%3!=0:
        f[n]=f[n-2]+f[n-3]
print(f[25])
