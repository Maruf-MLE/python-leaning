def sum(*num):
    
    print(num)
    sumetion = 0
    for x in num :
        sumetion = sumetion + x
    print(sumetion)
a=[2,5,3,4,6,7]
sum(*a)





# def student(*det):
#     print(det)

# student(100,'Maruf',101,'Abcd')

# xxarg

# def det(**details):     #Something Dictionary
#     print(details)

# det(id=1,Name='Maruf')