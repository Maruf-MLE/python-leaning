def voter(age):
    if age<=18:
        raise ValueError('invalid voter')
    return 'you are allowed to vote'
try:
    print(voter(5))

except ValueError as e:
    print(e)
print(voter(40))