# import re 
# import getpass
# nominal_password = r'(?=.*[A-Z])(?=.*[a-z])(?=.*[\d])(?=.*[!@#$%^&*])([A-za-z\d!@#$%^&*]){8,}'
# user_input_password = getpass.getpass()
# if re.search(nominal_password,user_input_password) and user_input_password[0].isupper():
#     print('ok')
# else:
#     print('no') 

import json
import getpass

with open('password.json') as file:
    my_dict = json.load(file)
file.close()    

while True:
    user = input('login--')
    password = getpass.getpass()
    if my_dict.get(user) == password:
        print('you ara wellcom')
        break         
    else:
        print('Your password or login are wrong\nplease enter again')
        continue

















