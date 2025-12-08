n=int(input())
list1=['1','2','3','4','5','6','7','8','9','0']
list2=['!','@','#','$']

# m=[a,c,d]

for j in range(n):# 变量名
    t=input()
    a,b,c,d=False,False,False,False
    invalid = False
    if len(t)>12 or len(t)<6:
        continue
    for i in t:
        if not (i.isalpha() or (i in list1) or (i in list2)):
            invalid = True
            break
        if i in list1:
            a=True
        elif i in list2:
            b=True
        elif i.isupper():
            c=True
        elif i.islower():
            d=True
    if not b:
        continue
    
    
    m = [a, c, d]
    # if m.count(True)<2:
    #     continue
    # else:
    if m.count(True) >= 2 and invalid == False:
        # print(a,c,d)
        print(t)