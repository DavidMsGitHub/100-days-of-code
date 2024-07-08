import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

cpu_score = []
cpu_score_num = 0
player_score = []
player_score_num = 0

def lose():
    print("You Lose!")
    play_again()

def win():
    print("You Win!!")
    play_again()

def add_random_card():
    return random.choice(cards)

def play_again():
    answer = input("Would you like to play blackjack again? (y/n): ")
    if answer == 'y':
        main_game()



## checks if players have blackjack or ace and fix
def check_blackjack():
    if 10 in cpu_score and 11 in cpu_score:
        lose()
    elif 10 in player_score and 11 in player_score:
        if 10 not in cpu_score and 11 not in cpu_score:
            win()


################


def main_game():
    cpu_score = []
    cpu_score_num = 0
    player_score = []
    player_score_num = 0

    for i in range(2):
        player_score.append(add_random_card())
        cpu_score.append(add_random_card())

    newcardginda = True
    while newcardginda == True:
        player_score_num = 0
        for final in player_score:
            player_score_num += final
        cpu_score_num = 0
        for final in cpu_score:
            cpu_score_num += final
        print(f"In your hand {player_score}, current score is {player_score_num}")
        print(f"Dealer's first card is {cpu_score[0]}")
        check_blackjack()
        if player_score_num > 21:
            if 11 in player_score:
                player_score_num - 10
                if player_score_num > 21:
                    lose()
                elif player_score_num < 21:
                    if input("Do you want to get another card? (y/n): ").lower() == 'y':
                        player_score.append(add_random_card())
                        newcardginda = False
            else:
                lose()
        else:
            if input("Do you want to get another card? (y/n): ").lower() == 'y':
                player_score.append(add_random_card())
            else:
                newcardginda = False

    while sum(cpu_score) < 17:
        cpu_score.append(add_random_card())


    print(f"In your hand {player_score}, current score is {player_score_num}")
    print(f"In Dealer's hand {cpu_score}, his current score is {sum(cpu_score)}")

    if cpu_score_num > 21:
        win()
    elif player_score_num > cpu_score_num:
        win()
    elif player_score_num == cpu_score_num:
        print("It's a draw!")
        play_again()
    elif cpu_score_num > player_score_num:
        lose()


main_game()


