import random 

target_number = random.randint (1, 10)

while True: 
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < target_number:
        print ("Too low")
    elif guess > target_number:
        print ("Too high")
    else : 
        print ("Correct")
        break
    