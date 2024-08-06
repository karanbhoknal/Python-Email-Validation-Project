# Python-Email-Validation-Project

# Email validation in python Using String function

# On Vscode 
  1 Create file email.py
  
# Start the code in python file 
# Email Validation in python ( using string function)]

email=input("Enter your Email: ")

k,j,d=0,0,0

if len(email)>=6:  #  here we have to count valid email length 

    if email[0].isalpha():      # you have 1st letter of gmail it should be alpha
    
        if ("@" in email) and (email.count("@")==1):
        
            if (email[-4]==".") ^ (email[-3]=="."):
            
                for i in email:
                
                    if i==i.isspace():
                    
                        k=1
                        
                    elif i.isalpha():
                    
                        if i==i.upper(): # W--  W==W 
                            j=1
                    elif i.isdigit():
                        continue
                        
                    elif i=="_" or i=="." or i=="@":
                    
                        continue
                        
                    else:
                    
                        d=1

                if k==1 or j==1 or d==1:
                
                    print("Wrong Email 5")
            else:
                print("Right Email ")
        else:
            print("Wrong Email 3")
    else:
        print('Wrong Email 2')                        
else:
    print("Wrong Email 1 ")


# You can run code on Terminal using this command

  1 python email.py

