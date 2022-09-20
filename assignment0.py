import re
import csv

# To check email valid or not
def email_validation(email):
  e_pattern =  r'\b[A-Za-z._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
  if(re.fullmatch(e_pattern, email)):
    return True 
  else:
    return False

#To check password valid or not
def password_validation(password):
  pass_pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$"
  if (re.fullmatch(pass_pattern, password)):
    return True 
  else:
    return False 

# To register new user
def register():
  mail = input("Enter your username : ")
  if email_validation(mail):
    password = input("Enter your password : ")
    if password_validation(password):
      with open("file.csv", "a", encoding='UTF-8') as parser:
        writer = csv.writer(parser)
        writer.writerow([mail, password])
        print("User registered successfully!")
    else:
      print("Invalid Password")
  else:
    print("Invalid Username")

# Function to Login
def login():
  with open("file.csv", "r") as file:
    reader = csv.reader(file)
    mail = input("Enter your username : ")
    password = input("Enter your password : ")
    for column in reader:
      if column[0] == mail:
        if column[1] == password:
          print("Login Successful")
          break
        else:
          print("Password Incorrect, Try again!")
          break
    else:
      print("User not registered")

#Function for Forgot password
def forgotpassword():
  with open("file.csv", "r") as file:
    reader = csv.reader(file)
    mail = input("Enter your username : ")
    for column in reader:
      if column[0] == mail:
        print("Your password - ",column[1])
        break 
    else:
      print("User not registered")


# Give option to Register/Login/Forgot_password
option = input("Select Option:\n1. Register\n2. Login\n3. Forgot Password\n")

# Conditions based on the user input options
if (option == "1"):
  register()
elif (option =="2"):
  login()
else:
  forgotpassword()