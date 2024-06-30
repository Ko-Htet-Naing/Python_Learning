import random;
menu_label = " roshambo game ".upper();
print(" ")
print(menu_label.center(40,"="))
print("Choose one of the three method".center(40))
print("Scissor".ljust(30, ".") + "1".rjust(10))
print("Hand".ljust(30,".") + "2".rjust(10))
print("Paper".ljust(30,".") + "3".rjust(10))
print(" ")

# To control user play histroy
success_count = 0;
lose_count = 0;
match_count = 0;
draw_count = 0;

def determine_result(userChoice,systemChoice) :
    global success_count, lose_count, match_count,draw_count;
    if(userChoice == systemChoice) :    
        draw_count+=1;
        match_count = match_count + 1;
        return " Draw ";
    elif (userChoice ==1 and systemChoice == 3) or \
        (userChoice == 2 and systemChoice == 1) or \
        (userChoice  == 3 and systemChoice == 2) :
        success_count = success_count + 1;    match_count = match_count + 1;
        return " You Win ";
    else : 
        lose_count = lose_count + 1;    match_count = match_count + 1;
        return " You Lose ";


def generate_random_number(): 
    return random.choice([1,2,3])

def name_of_choice(choice):
    choices  = {
        1 : "Scissor",
        2 : "Hand",
        3 : "Paper"
    }
    return choices.get(choice,"Invalid Choice")
def prety_output(userChoice, systemChoice) :
    print(" ")
    print("user choice ".ljust(20," ") + ":".ljust(5," ") + name_of_choice(userChoice))
    print("system choice ".ljust(20," ") + ":".ljust(5," ") + name_of_choice(systemChoice))
    print(" ")

def center_print(showData):
    print(showData.center(40,"="));
    print(" ")

# accept user input 
user_choice_random_value = int(input("Please choose one option 1, 2 or 3 : "))
# Exit from game when user type 0
while (user_choice_random_value != 0) :
    # Validate User Input
    while(user_choice_random_value not in [1,2,3] or user_choice_random_value == 0):
        print("Invalid format. Please choose 1, 2 or 3")
        user_choice_random_value = int(input("Please choose one option 1, 2 or 3 : "))
        break;
    
    # when user choose 0 under the first while loop
    if(user_choice_random_value == 0) : break;

    # generate system choice
    system_choice_random_value = generate_random_number();
    match_result = determine_result(user_choice_random_value, system_choice_random_value);
    prety_output(user_choice_random_value,system_choice_random_value)
    center_print(match_result)
    user_choice_random_value = int(input("Please choose one option 1, 2 or 3 : "))
print(f"During this {match_count} matches. You win {success_count} match, {lose_count} lose and {draw_count} draw.")
print("Bye Bye see you again.")