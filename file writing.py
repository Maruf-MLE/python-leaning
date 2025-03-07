file=open('text.txt','w')

file.write('\nMy name is maruf')
file=open('text.txt','r')
text=file.read()
print(text)
file.close()