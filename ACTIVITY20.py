from getpass import getpass

r='rungwoo'
c='sindipot0402'

isLogin= False #trigger

while isLogin == False:
    user=input('username:')
    password=input('password:')
    if user==r and password==c:
        print('ACCESS GRANTED')
        isLogin = True
    else:
        print('ACCESS DENIED')
        isLogin = False
        break

