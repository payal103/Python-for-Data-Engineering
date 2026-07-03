# project
# 1 recive an email from the user 
# 2 validate the email
# 3 if it is invalide log the error in a File Exists Error
# 4 if it is valid Clean and structure the email 
# 5 log each step of the program



#importing required libraries
from datetime import datetime
#for loging the date of the action


#function for wring logs
def write_log(message):
    with open("app.log", "a") as file:#createing a file using append mode"a"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {message}\n")

#function for reciveing the email from the user
def get_email():
    write_log("Asking user for email")
    email = input("Enter your email: ")
    write_log("User entered an email")
    return email

#function to vadidate the email
def validate_email(email):

    if "@" not in email:
        write_log("Validation Failed : @ symbol missing")
        return False

    if "." not in email:
        write_log("Validation Failed : . symbol missing")
        return False

    write_log("Email validated successfully")
    return True

#function if the email is validate it will clean the email 
def clean_email(email):

    write_log("Cleaning email")

    email = email.strip()#clean the empty spaces

    email = email.lower()#lower the string 

    write_log("Email cleaned")

    return email


#mail code to run all the functions together 

write_log("Program Started")

email = get_email()

if validate_email(email):

    email = clean_email(email)

    print(email)

write_log("Program Finished")