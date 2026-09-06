attempts = 0
max_attempts = 5

while attempts < max_attempts:
    username = input("Enter username:")
    password = input("Enter password:")

    if username == "Python" and password == "rules":
        print("Welcome")
        break 
    else:
        attempts += 1 

    if attempts == max_attempts :
        print ("Access denied")
        