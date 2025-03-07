
# def dup():
#     l=input('enter your list')
#     l1=list(map(int,l.split( )))
#     l2=[]
#     for x in l1:
#         if x not in l2:
#             l2.append(x)
#     return l2


# r=dup()
# print(r)

# def rev():
    
#     l1=[1,2,3,4,5,6]
#     l2=[]
#     for j in range(1,7):
#         l2.append(l1[-j])
#     return l2
# r=rev()
# print(r)

#tow sum
class solution:
    def towsum(self,nums:list[int],target:int) ->list[int]:
        hashmap={}
        for index,num in enumerate(nums):
            complement=target-num
            if complement in hashmap:
                return [hashmap[complement],index]
            hashmap[num]=index
        return []

    
a = [1,3,2, 7, 11, 15]
b = 9
r=solution()
s=r.towsum(a,b)
print(s)

            


