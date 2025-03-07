class phone:
    def __init__(self):
        print('i am a phone class')
class realme(phone):
    def __init__(self):
        super().__init__()
        print('i am a realme class')

r=realme()