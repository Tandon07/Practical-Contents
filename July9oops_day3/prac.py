l=[10,2,3,4,5,5,5,6,6,7,10,[11,22,33,44,55,66],111,222,333,234,'umesh']
# # l1=[]
# # l1=l[0]
# # j=0
# # for i in l[1::]:
# #     if(type(i)==int):
# #         if (l1[j]!=i):
# #             l1.append(i)
# #
# #         else:
# #             pass
# c=0
# print(l)
# for i in l:
#     for j in l:
#         if(i==j):
#             c=c+1
#             if(c>0):
#                 for k in range(c+1):
#                     l.remove(i)
#     print(i," ",c)
#     c=0
#
l1 = []
for i in l:
    if type(i)==int :
        l1.append(i)
    if type(i) == list or type(i) ==tuple or type(i)==set:
        for j in i :
            if type(j) == int or type(j) == str:
                l1.append(j)
    if type(i) == dict :
        for k in i.items() :
            for g in k :
                if type(g) == int  or type(g) == str:
                    l1.append(g)
print(l1)
for i in set(l1):
    print(i, " ----> ", l1.count(i))
