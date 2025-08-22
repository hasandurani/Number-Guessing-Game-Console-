import random
print("Welcome To Number Guessing Game...")
print("You Have Only 10 Attempts")
secret_num=random.randint(1,50)
attempts=10

while True:
    user = int(input("Guess The Number From (1-50): "))
    attempts -= 1
    if user<secret_num:
        print("Too Low Brother...")
    elif user>secret_num:
        print("Too High Brother...")
    elif user == secret_num:
        print(f"You Won , The number is {user}")
        break
    if attempts == 0:
        print("Game Over! You Lose")
        break
    else:
        print("Attempts left:", attempts)
    
