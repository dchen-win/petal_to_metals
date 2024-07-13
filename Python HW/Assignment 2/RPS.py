import random
print("Welcome to Rock, Paper, Scissors")
while True:
    user_input = int(input("Choose your implment! (1= Rock, 2= Paper, 3= Scissors, 0 = Quit): "))
    if user_input!= 0:
        computer_input = random.randint(1,3)
        print(f"You picked {user_input} and the computer picked {computer_input}")
        if user_input == computer_input:
            print("It's a draw!")
        elif user_input == 1:
            if computer_input == 3:
                print("You win!")
            else:
                print("You lose!") 
        elif user_input == 2:
            if computer_input == 1:
                print("You win!")
            else:
                print("You lose!") 
        elif user_input == 3:
            if computer_input == 2:
                print("You win!")
            else:
                print("You lose!")
    else:
        print("Thanks for playing!")
        break