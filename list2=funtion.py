sub=['c','c++','java','python','os','toc','os']
# print(len(sub))      {lenth detected}
# sub.append("toc")    {add element}
# print(sub)
sub.insert(2,"html")       #{Adds an element at the specified position}
print(sub)
sub.remove('toc')
# sub.sort()
# sub.reverse()
# sub.pop()              {Removes the element at the specified position}
# sub.clear()
sub2=sub.copy()
print(sub2)
pos=sub.index("java")   #{ position detected}
print(pos)
count=sub.count("os")   # count this total item
print(count)

