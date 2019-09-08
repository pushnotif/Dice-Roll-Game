import random

# loop for the whole game
try_again = True

while  try_again == True:

    # prompt user for number of dice rolls
    num_rolls = int(input("Enter number of dice rolls: "))

    # variables for dice value and count for loop statement
    dice_value = [1, 2, 3, 4, 5, 6]
    count = 0

    # loop statement for number of rolls results

    while count < num_rolls:
            print(random.choice(dice_value))
            count = count + 1

    # prompt user to play again

    try_again = input("Would you like to roll again? (y/n): ")
    if try_again == "y":
        try_again = True
    else:
        try_again = False

print("Thanks for playing")