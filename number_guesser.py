import random

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please Type a number larger than 0 next time.')
        quit()
else: 
    print("Please type a number next time.")
    quit()

random_number = random.randint(-10, 11)
print(random_number)

while True:
    user_guess = input("Make a guess: ")
    break

