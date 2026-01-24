import random

def game(user, computer):
    if user == computer:
        return None
    elif user == 's':
        return computer == 'w'
    elif user == 'w':
        return computer == 'g'
    elif user == 'g':
        return computer == 's'

print("Snake Water Gun Game")
print("Choose:")
print("s = Snake")
print("w = Water")
print("g = Gun")

user_choice = input("Enter your choice (s/w/g): ").lower()
computer_choice = random.choice(['s', 'w', 'g'])

print(f"You chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

result = game(user_choice, computer_choice)

if result is None:
    print("It's a tie!")
elif result:
    print("You win!")
else:
    print("You lose!")
