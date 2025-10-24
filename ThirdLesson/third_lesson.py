#even or odd
def even_or_odd(number):
    even = number % 2
    if even == 0:
        print("четное")
    else:
        print("нечетное")

even_or_odd(7)




#login and password
def login_and_password(input_login, input_password):
    credentials = [{'login' :"alice", 'password':"qwerty"}, {'login':"bob", 'password':"12345678"}]
    for user in credentials:
        if user['login'] == input_login and user['password'] == input_password:
            print('Access Granted')
            return
    print('Incorrect login or password')

login_and_password('alice','12345678')
