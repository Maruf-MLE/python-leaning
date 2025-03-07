result=[i for i in range(11) if i%2==0 ]
print(result)
result2=[(i,j) for i in range(7) for j in range(7) if j%2==0 if i%2==0 ]
print(result2)