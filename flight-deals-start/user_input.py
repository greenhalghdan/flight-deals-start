from data_manager import DataManager
email_address = "1"
confirm_email = "2"
attempt = 0
print("Welcome to Dans flight Club")
print("We find the best deals and email you.")
first_name = input("What is your first name? \n")
last_name = input("Whats is your last name? \n")
email_address = input("Whats if your email address? \n")
while email_address != confirm_email:
    confirm_email = input("Please confirm your email address: \n")
    if attempt > 1:
        print("That didn't seem to match.")
    attempt += 1
input = DataManager()
upload_user = input.user_input(first_name, last_name, email_address)
print(upload_user)