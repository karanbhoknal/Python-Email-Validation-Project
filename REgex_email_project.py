# email validation in  python [using Regex]
# Here all condition we have
# a-z
# 0-9 
# . _ time 1
# @ time 1
# .  2,3 position of dot 


import re 
#  when are search some character that we can use [\]
# 0-9 we have only one value that is why we can use [?]
# It is work for  search [@]
# any character or string we have this string or character search work of [\w]
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input('Enter your Email:')

# Here we are using if condition and we are doing pass email_condition and email_user

if re.search(email_condition,user_email):
    print("Right Email")
else:
    print("Wrong Email")
    
