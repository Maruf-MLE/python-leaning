
a=20
b=0
try:
    result=a/b
    print(result)
except (ZeroDivisionError,ValueError):
    print('zero is not working for dividing')
finally:
    print('all done')
print('succesfull')
try:
    a=int(input('a=?'))
    b=int(input('b=?'))
    r=a/b
    print(r)
except (ValueError,ZeroDivisionError):
    print('value or zeroDivition error')




