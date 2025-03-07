

# int data type
Hablu = 420
print(type(Hablu))

#floating type data
dablu = 40.456
print(dablu)
print(type(dablu))

#complex type data
kodu=40j          #only (j) & only Int
print(type(kodu))

# str type data
he="Maruf"
she='female'
print("my name is"+' ' + he)
print(type(he))


#Boolean data type
bol=True  #first letter captital letter
print(type(bol))

x=5
y=10
z=10
print(x > y)
print(y==z)
print(y<=z)

#binary byteArray data type
list2=[1,2,4,7,9,5,6,255]     #0-256 in range
b1=bytearray(list2)           #list data type convert convert to bytearray data type
b1[0]=100                 #Bytearray data type value is changeable
print(type(b1))
print(b1[0])
print(list2)

#binary byte data type
list=[1,2,4,7,9,5,6,255]     #0-256 in range
b=bytes(list)          #list data type convert to byte data type
print(list)
print(type(b))




#list type data
li=["maruf","hablu",'ishant']   #value is muteable
li[0]='developer'
print(li)
print(type(li))


#list type data
li2=("maruf","hablu",'ishant')  #value is not muteable

print(li2)
print(type(li2))
