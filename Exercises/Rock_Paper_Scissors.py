import random
print("\033[4mWelcome to my rock/paper/scissors game!\033[0m")
user_score = 0
ai_score = 0
computer_pick = ()
user_input = ()


def score_count(user_score, ai_score):
    print(f'Your score is: {user_score} and computer score is: {ai_score}')


playing = str(input('''Do you want to play with me?
If yes type "yes", if no type "no". > '''))

if playing.lower() != "yes":
    print("Have a good day!")
    quit()
else:
    print("Let's play then!")

    while user_input != "q" and user_score < 10 and ai_score < 10:
        user_input = str(input('''Press 'r' for \U0001FAA8;
Press 'p' for \U0001F4DC;
Press 's' for \u2702;
Press 'q' to quit. ''')).lower()

        if user_input == "q":
            print("Nice playing with you!")
            quit()
        elif user_input in ["r", "p", "s"]:
            ai_pick_number = random.randint(0, 2)
            options = ["rock", "paper", "scissors"]
            computer_pick = options[ai_pick_number]

            if user_input == "r" and computer_pick == "scissors":
                print('You have picked \U0001FAA8, computer picked \u2702. you win!')
                user_score += 1
                score_count(user_score, ai_score)
            elif user_input == "r" and computer_pick == "paper":
                print('You have picked \U0001FAA8, computer picked \U0001F4DC. you lose!')
                ai_score += 1
                score_count(user_score, ai_score)
            elif user_input == "r" and computer_pick == "rock":
                print("You have picked \U0001FAA8, computer picked \U0001FAA8. It's a draw!")
                score_count(user_score, ai_score)
            elif user_input == "p" and computer_pick == "rock":
                print('You have picked \U0001F4DC, computer picked \U0001FAA8. you win!')
                user_score += 1
                score_count(user_score, ai_score)
            elif user_input == "p" and computer_pick == "scissors":
                print('You have picked \U0001F4DC, computer picked \u2702. you lose!')
                ai_score += 1
                score_count(user_score, ai_score)
            elif user_input == "p" and computer_pick == "paper":
                print("You have picked \U0001F4DC, computer picked \U0001F4DC. It's a draw!")
                score_count(user_score, ai_score)
            elif user_input == "s" and computer_pick == "paper":
                print('You have picked \u2702, computer picked \U0001F4DC. you win!')
                user_score += 1
                score_count(user_score, ai_score)
            elif user_input == "s" and computer_pick == "rock":
                print('You have picked \u2702, computer picked \U0001FAA8. you lose!')
                ai_score += 1
                score_count(user_score, ai_score)
            elif user_input == "s" and computer_pick == "scissors":
                print("You have picked \u2702, computer picked \u2702. It's a draw!")
                score_count(user_score, ai_score)
        else:
            print("You can only type r,p,s or q! ")
print('Final score is:')
print(f'{user_score} points for you, {ai_score} points for the computer!')
if user_score > ai_score:
    print('\033[4mYou win!\033[0m')
else:
    print('\033[4mComputer wins!\033[0m')

print("END OF PROGRAM!")
