# list1=[1,2,3,4,5,6]
# list2=['maruf','ppp','ttt','eee','eee','yyy']
# result=list(zip(list1,list2,'abcdef'))
# print(result)

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]
r=list(zip(names,scores,'abcdef'))
print(list(r))
for n,s,p in r:
    print(f"{n} point is: {s} and gread is:{p}")

