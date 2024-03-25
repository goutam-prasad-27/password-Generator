import random, string

# All Defined Character Sets:
lower_case= string.ascii_lowercase
upper_case= string.ascii_uppercase
symbols= string.punctuation
digits= string.digits

# Password Generation Function:
def passGen(len, add_upper=True, add_digit=True, add_symbols=True):
    """ ::'THIS FUNCTION HELPS TO GENERATE THE PASSWORD ITSELF'::
        len : DECIDES THE LENGTH OF PASSWORD
        add_upper : DECIDES WHETHER TO USE UPPERCASE IN PASSWORD
        add_digit : DECIDES WHETHER TO USE NUMBERS IN PASSWORD
        add_symbols : DECIDES WHETHER TO USE SYMBOLS IN PASSWORD
    """
    all_Char= ""
    if add_upper:               #adds uppercase letters in password
        all_Char+= upper_case
    if add_digit:               #adds lowercase letters in password
        all_Char+= digits
    if add_symbols:             #adds symbols letters in password
        all_Char+= symbols
    all_Char+= lower_case       #adds lowercase letters in password

    passWord= "".join(random.sample(all_Char,len))      #joins all the parameters together to form a password
    return passWord                                     #returns the password

# Getting UserInput To Generate The Password
length= int(input("ENTER DESIRED PASSWORD LENGTH:   "))
upper= input("INCLUDES UPPERCASE (y/n) ?:  ").lower() == 'y'
sym= input("INCLUDES SYMBOLS (y/n) ?:  ").lower() == 'y'
nums= input("INCLUDES NUMBERS (y/n) ?:  ").lower() == 'y'

# Calling The Function To Run And Fetch The Password
generate= passGen(length, upper, nums, sym)
print('Password:', generate)
