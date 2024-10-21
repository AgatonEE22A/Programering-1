corrPass = "password"
corrUser = "Agaton"

username = input("username: ")
password = input("password: ")

if username == corrUser:
    print("Correct user: " + corrUser)
else:
    print("Wrong username: " + username)

if password == corrPass:
    print("Correct password: " + corrPass)
else:
    print("Wrong password: " + password)
