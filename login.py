import re 
import getpass
nominal_password = r'(?=.*[A-Z])(?=.*[a-z])(?=.*[\d])(?=.*[!@#$%^&*])([A-za-z\d!@#$%^&*]){8,}'
user_input_password = getpass.getpass()
if re.search(nominal_password,user_input_password) and user_input_password[0].isupper():
    print('ok')
else:
    print('no')    