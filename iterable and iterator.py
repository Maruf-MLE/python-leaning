list1=[2,5,7,9]
list2=list(enumerate(list1))
print(list2)
it=iter(list2)
print(list2)
print(next(it))
print(next(it))
print(next(it))

list4=zip(list1,list2)
print(list4)
