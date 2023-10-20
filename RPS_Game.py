# Rock Paper Scissors Homework
#random.choices. 
import random 

def game():


    loser_emoicon =  "(╯°□°)╯︵ ┻━┻"

    winner_emicon = "(-■_■)"

    android_options = ["Rock", "Paper", "Scissors"]



    while True:
        option_for_android = random.choice(android_options)
        # Debug only
        # print(option_for_android)
        user_input = input("Choose \'Rock\', \'Paper\' or \'Scissors\' or \'quit\' to quit \n").lstrip().title().rstrip()
        
        # Debug Only
        # print(user_input)

        loser = False

        if user_input == option_for_android:
            print("It's a tie!")
        elif user_input == "Rock" and option_for_android == "Paper":
            print("Paper covers rock loser!", loser_emoicon)
            loser = True

        elif user_input == "Rock" and option_for_android == "Scissors":
                print("Rock crushes Scissors. You win",winner_emicon)
        elif user_input == "Quit":
            print("Quitter")
            break
        elif user_input == "Paper" and option_for_android == "Rock":
            print("Paper covers Rock, you win!", winner_emicon)
        elif user_input == "Paper" and option_for_android == "Scissors":
            print("Scissors cuts Paper, you lose.", loser_emoicon)
            loser = True

        elif user_input == "Scissors" and option_for_android == "Rock":
            print("Rock crushes Scissors. You loses." , loser_emoicon)
            loser = True

        elif user_input == "Scissors" and option_for_android == "Paper":
            print("Scissor cuts Paper. You Win.",winner_emicon)
        else: 
            print("option skipped")

        quitter = False

        if loser== True:
            # This loops unitl they choose whether or not to quit.
            while True:
                wants_to_play = input("Play Again? \'yes\' or \'no\'").lower().strip()
                if wants_to_play == "no":
                    print("Quitter")
                    quitter = True
                    break
                elif wants_to_play == 'yes':
                    break
                else:
                    print("I didn't quite get that.")
        if quitter == True:
            break

game()

        

