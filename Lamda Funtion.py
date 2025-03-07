list1=[1,2,3,4,5,6]
for y in list1:
    print(y)

    bachay=list(map(lambda x:'odd' if x%2==0 else 'even',[y]))
    print(bachay)