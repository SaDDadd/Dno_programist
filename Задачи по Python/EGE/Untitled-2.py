# for x in range(0,2):
#     for y in range(0,2):
#         for z in range(0,2):
#             for w in range(0,2):
#                 if False==(not(z and not w) or ((not z or w)==(not x or y))):
#                     print(x ,'', y ,'', z ,'', w ,'')
# chislo=4**625-2**311+2**571-48
# f1=0
# while chislo:
#     if chislo%4==1:
#         f1+=1
#     chislo//=4
# print(f1)
v=0
for a in range(1000,1,-1):
    for x in range(1,1001):
        if (not(x%13==0) or not(40<=x<=60)) or(a<x+20):
            v+=1
    if v==1000:
        print(a)
        
            
    
    