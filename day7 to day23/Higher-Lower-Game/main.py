import random
from art import logo
from art import vs
from replit import clear
from game_data import data

score = 0

print(logo)
random_chooser_a = random.choice(data)
############## Aqet Funqciebia ####################


#Function To return correct answer
def check_followers(person_a, person_b):
    followers_b = random_chooser_b['follower_count']
    followers_a = random_chooser_a['follower_count']
    if followers_a > followers_b:
        return person_a
    elif followers_b > followers_a:
        return person_b

#Function to check for correct answer
def check_answer():
    global score
    global answer
    global correct
    global random_chooser_a
    if answer == correct:
        score += 1
        print(f"You're right! your scores: {score}")
        random_chooser_a = answer
        clear()
        data.remove(random_chooser_b)
        if len(data) == 1:
            print("Congrats you've won the whole game, Bye!")
            exit()
        else:
            main_game()
    else:
        print(f"You're wrong! You lost")


# Main game, i created this function to loop the game if answer is correct (sxvanairad damezara fiqri :D)
def main_game():
    global random_chooser_b
    global answer
    global correct
    global random_chooser_a
    global check_answer
    print(f"Compare A: {random_chooser_a['name']}, {random_chooser_a['description']}, from {random_chooser_a['country']}\n")

    print(f"\n{vs}\n")

    random_chooser_b = random.choice(data)
    print(f"Against B: {random_chooser_b['name']}, {random_chooser_b['description']}, from {random_chooser_b['country']}")

    # Correct = real answer and answer = players choice

    correct = check_followers(random_chooser_a, random_chooser_b)

    answer = input(f"Choose A or B (CHEAT: Answer is {correct}: ").lower()

    if answer == "a":
        answer = random_chooser_a
    elif answer == 'b':
        answer = random_chooser_b
    check_answer()


#################################################


main_game()







