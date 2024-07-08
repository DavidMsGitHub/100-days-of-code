import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def add_random_card():
    return random.choice(cards)

def play_again():
    answer = input("Would you like to play blackjack again? (y/n): ")
    return answer.lower() == 'y'

def check_blackjack(cpu_score, player_score):
    if 10 in cpu_score and 11 in cpu_score:
        return 'cpu'
    elif 10 in player_score and 11 in player_score:
        return 'player'
    return None

def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score

def main_game():
    while True:
        cpu_score = [add_random_card(), add_random_card()]
        player_score = [add_random_card(), add_random_card()]

        print(f"In your hand {player_score}, current score is {sum(player_score)}")
        print(f"Dealer's first card is {cpu_score[0]}")

        if check_blackjack(cpu_score, player_score) == 'cpu':
            print("You Lose!")
        elif check_blackjack(cpu_score, player_score) == 'player':
            print("You Win!!")
        else:
            while calculate_score(player_score) < 21:
                if input("Do you want to get another card? (y/n): ").lower() != 'y':
                    break
                player_score.append(add_random_card())
                print(f"In your hand {player_score}, current score is {sum(player_score)}")

            player_score_num = calculate_score(player_score)
            if player_score_num > 21:
                print("You Lose!")
            else:
                while calculate_score(cpu_score) < 17:
                    cpu_score.append(add_random_card())

                cpu_score_num = calculate_score(cpu_score)
                print(f"In your hand {player_score}, current score is {player_score_num}")
                print(f"In Dealer's hand {cpu_score}, his current score is {cpu_score_num}")

                if cpu_score_num > 21 or player_score_num > cpu_score_num:
                    print("You Win!!")
                elif player_score_num == cpu_score_num:
                    print("It's a draw!")
                else:
                    print("You Lose!")

        if not play_again():
            break

main_game()