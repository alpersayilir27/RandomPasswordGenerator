import random
import string

lenght = int(input("Enter the lenght of the password: "))

chars = string.ascii_letters
chars += string.digits
chars += string.punctuation

password = ""

for i in range(lenght):
    password += random.choice(chars)
   
print(f"Your random passwords is:{password}")