import random
from time import sleep
Chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()'

while 1:
    password_len = int(input("What length would you like your password to be : "))
    password_count = int(input("How many passwords would you like : "))
    for x in range(0, password_count):
        password = ""
        for x in range(0, password_len):
            password_char = random.choice(Chars)
            password = password + password_char
        print("Here is your random password : ", password)

        if password != "":
            file = open('passwords.txt', 'a')
            file.write(password+"\n")
            file.close()
            print("Added Password to Text File.")
            sleep(2)