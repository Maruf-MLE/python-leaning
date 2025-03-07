class phone:
    def cal(self):
        print('you can call')
    def msg(self):
        print('you can msg')
class realme(phone):
    def photo(self):
        print('you can take photo')

r=realme()
r.photo()
r.cal()
r.msg()
