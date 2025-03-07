#তালিকা একটি সংগ্রহ যা আদেশ এবং পরিবর্তনযোগ্য. ডুপ্লিকেট সদস্যদের অনুমতি দেয়।
sub = ['c','c++','java','python','os','toc']

print(sub)    #print all item in list
print(sub[0])   #print 0  number item in the 
print(sub[2:])   # print start at value number 2
print(sub[-1]) # print in the reverse side

print("java"in sub)  # check the python word in our list 
print("java" not in sub)  # check the python word in our list 
print(sub+["swift",55]) # add the new item in list 
print(sub * 3)  # list will be convert triple item


n= input('enter your all marks')

list = n.split()
sum = 0
for x in list :
    sum= sum + int(list)
    print(sum)