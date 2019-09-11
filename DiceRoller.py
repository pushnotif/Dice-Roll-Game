import random

# loop for the whole game
try_again = True

while  try_again == True:

    # prompt user for number of dice rolls
    num_rolls = int(input("Enter number of dice rolls: "))
    num_side = int(input("Enter number of sides: "))

    # variable for count variable for loop statement
    count = 0

    # loop statement for number of rolls results

    while count < num_rolls:
            # variables for dice value, "num_side+1" since last item isn't considered
            # i.e for 10 sided dice, 10 wont be picked as a result if rolled
            dice_value = random.randrange(1, num_side + 1, 1)
            print("You roll: ",dice_value)
            count = count + 1

    # prompt user to play again

    try_again = input("Would you like to roll again? (y/n): ")
    if try_again == "y":
        try_again = True
    else:
        try_again = False

print("Thanks for playing")
