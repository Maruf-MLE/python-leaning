class student:
    roll=''
    gpa=''
rahim=student()
print(isinstance(rahim,student))
rahim.roll=101
rahim.gpa=3.92
print(f'Rahim roll:{rahim.roll} or gpa:{rahim.gpa}')
karim=student()
karim.roll=102
karim.gpa=3.95
print(f'karim roll:{karim.roll} or gpa:{karim.gpa}')
maruf=student()
maruf.roll=103
maruf.gpa=3.96
print(f'maruf roll:{maruf.roll} or gpa:{maruf.gpa}')