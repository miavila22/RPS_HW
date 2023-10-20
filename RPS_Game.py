# Rock Paper Scissors Homework
#random.choices. 
import random 

#while True Loops 

android_options = ["Rock", "Paper", "Scissors"]
while True:
    option_for_android = random.choice(android_options)
    print(option_for_android)
    user_input = input("Choose Rock, Paper or Scissors \n").lstrip().title().rstrip()
    print(user_input)
    if user_input == option_for_android:
        print("It's a tie!")
    elif user_input == "Rock" and option_for_android == "Paper":
        print("Paper covers rock loser! (╯°□°)╯︵ ┻━┻")
    
    elif user_input == "Rock" and option_for_android == "Scissors":
            print("Rock crushes Scissors")
    elif user_input == "Quit":
         print("Quitter")
         break
    elif user_input == "Paper" and option_for_android == "Rock":
         print("Paper covers Rock, you win!")
    elif user_input == "Paper" and option_for_android == "Scissors":
        print("Scissors cuts Paper, you lose (╯°□°)╯︵ ┻━┻")    
    else: 
        print("option skipped")

        

