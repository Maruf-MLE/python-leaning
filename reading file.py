file=open('text.txt','r+')
# text=file.read()
# print(text)
# size=len(text)
# print(size)
# line1=file.readline()
# print(line1)
# line=file.readlines()[3]
# print(line)
# file.close()
files=file.readlines()
print(files)
for line in files:
    print(line.strip())

