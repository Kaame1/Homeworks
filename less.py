# Passwor
import getpass
import re
import json

with open('password.json') as file:
    my_dict = json.load(file)
file.close()    

nominal_password = r'(?=.*[A-Z])(?=.*[a-z])(?=.*[\d])(?=.*[!@#$%^&*])([A-za-z\d!@#$%^&*]){8,}'

while True:
    user_input_login = input('Login---')
    for i in my_dict:
        if i == user_input_login:
            print('Your login is already existing\nplease enter oder login') 
            continue
    user_input_password = getpass.getpass()    
    if (re.search(nominal_password, user_input_password)): 
        my_dict.setdefault(user_input_login,user_input_password)      
        print('Your password is strong')
        with open('password.json', 'w') as file:
            json.dump(my_dict, file)
        file.close() 
        break
    else:
        print('Your password is not strong\nplease enter angen')
        continue
        


