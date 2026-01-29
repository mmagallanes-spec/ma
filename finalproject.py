#Mariio Magallanes
# Final Project
# GitHub test comment


#this is a function for option 5
def temperature_c_to_f():

    f = float(input("Please enter the current temperature in degrees fahrenheit: "))
    c = (f-32)*(5/9)
    print("YOur current temparute in degrees Celsius is ",c)

#this is a function for option 6
import random
def dice_roll():
    r = random.randint(1, 6)
    name = input("Enter your name: ")
    print("Welcome to the Dice Rolling Game!", name)
    r = random.randint(1, 6)  # Generate the random number here
    g = 0
    while g != r:
        g = int(input("Enter your lucky guess: "))
        
        if (g < 1) or (g > 6):
            print("Your number is out of range \U0001F480")    
        elif g > r:
            print("Your guess is too big! Please try again. \U0001F480")
        elif g < r:
            print("Your guess is too small! Please try again. \U0001F480")
        else:
            print("Thank you for playing! You may exit the game now! \U0001F600")
        

def rock_paper_scissors():
    o = ("rock", "paper", "scissors")
    c = random.choice(o)
    #print("Computer chose:", c)
    u = input("Enter your choice (rock, paper, or scissors): ")
    if u == c:
        print("It's a tie! \U0001F610")
    elif (u == "rock" and c == "scissors"):
        print("You win! \U0001F600")
    elif (u == "rock" and c == "paper"):
        print("Computer wins! \U0001F480")
    elif (u == "paper" and c == "rock"):
        print("You win! \U0001F600")
    elif (u == "paper" and c == "scissors"):
        print("Computer wins! \U0001F480")
    elif (u == "scissors" and c == "paper"):
        print("You win! \U0001F600")
    elif (u == "scissors" and c == "rock"):
        print("Computer wins! \U0001F480")

#option 0
option = 0

name = input("What is your name:")
print("Greeetings", name, "Please select a choice from the following menu.")

print("***************")
print("\U0001F602"*9)
print("Option 1")
print("Option 2")
print("Option 3")
print("Option 4")
print("Option 5")
print("Option 6")
print("***************")
print("\U0001F602"*9)

option = int(input("Option:" ))

#option 1
if option == 1:
    print("Why do scientist trust atoms?")
    print("beacuse they make up everything!")

#option 2
if option == 2:
    for i in range(15):
        print("Hello", name)

#option 3
if option == 3:
    number = int(input("Enter a number:"))
    for i in range(number):
        print("Do, or Do not. There is no try.")

#option 4
if option == 4: 
    g = -1
    n = 25
    print("This is a Lucky Number Game.")
    print("Your entry must be between 0-100.")

    while g != n:
        g = int(input("Enter your lucky guess: "))
        
        if (g < 0 ) or (g > 100):
            print("Your number is out of range")
#            g = int(input("Enter your lucky guess: "))

        elif (g > n):
            print("Your guess is too big! Please try again.")

        elif (g < n):
            print("Your guess is too small! Please try again.")
    
        else:
            print("Thank you, your guess is the Lucky Number.")

#option 5 
if option == 5:
    
    celsius = temperature_c_to_f()
    
#option 6
if option == 6:
    for i in range(100):
        print("\n")
        print("Welcome to the final stage of the game")
        print("You now only have 3 choices")
        print("\U0001F480" * 10)
        print("Door 1")
        print("Door 2")
        print("Door 3")
        print("\U0001F480" * 10)
        print("The only way to escape is to above expectations. \n")
        door = int(input("Choose a door (1, 2, or 3): "))
    # Door 1
        if door == 1:
            dice_roll()
    # Door 2
        elif door == 2:
            rock_paper_scissors()
    # Door 3
        elif door == 3:
            number = int(input("Enter a number: "))
            for i in range(number):
                print("There is no way out of this game! \U0001F480")
        else:
            break



