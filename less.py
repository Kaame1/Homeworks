# Passwor
import time
import getpass
import re
import json

with open('password.json', 'w') as file:
    file.close()

user_input_login = input('Login---')
nominal_password = r'(?=.*[A-Z])(?=.*[a-z])(?=.*[\d])(?=.*[!@#$%^&*])([A-za-z\d!@#$%^&*]){8,}'

while True:
    x = {}
    user_input_password = getpass.getpass()
    if (re.search(nominal_password, user_input_password)):
        x = {'login':user_input_login, 'password':user_input_password}       
        print('Your password is strong')
        with open('password.json', 'a') as file:
            json.dump(x, file)
        file.close() 
        break
    else:
        print('Your password is not strong\nplease enter angen')
        continue
            