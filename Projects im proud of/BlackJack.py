import random

card_dict = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
    10: 'Ten',
    11: 'Jack',
    12: 'Queen',
    13: 'King',
    14: 'Ace'
}


# TODO get correctly if statements on last function of blackjack game
#  write down/comment code
#  annotate/comment functions


def user_card_game():
    # Variables initiated
    score = 0
    start_point = 0
    blackjack = 21
    # while loop shall spin until score is not more then 21 or until
    # user decides to stop so he could compare his score to COMPUTER score
    while score < blackjack:
        # below line generates random key for dictionary
        random_key = random.randint(start_point + 1, len(card_dict))
        # below line keeps score of total cards in hand
        score += random_key
        # below line generates random card from deck
        random_card = card_dict.get(random_key)
        print('*' * 100)
        print()
        if score > blackjack:
            print("Last card was {}".format(random_card))
            print("Total score was {}".format(score))
            print("Better luck next time!")
            return score
        elif score == blackjack:
            print("BlackJACK!")
            return score
        user_input = input("You got {}, total is now {} would you like "
                           "another one? (Y/N): ".format(random_card, score))
        if user_input == "y":
            continue
        if user_input == "n":
            return score


# user_card_game()


def pc_card_game():
    score = 0
    start_point = 0
    blackjack = 21
    hand_list = []
    while score <= blackjack:
        random_key = random.randint(start_point + 1, len(card_dict))
        score += random_key
        random_card = card_dict.get(random_key)
        hand_list.append(random_card)

        if blackjack >= score > + 19:
            print("PC has got {}".format(score))
            print("PC hand contains {}".format(hand_list))
            print()
            return score
        if score > 21:
            print("Shitty score was {}".format(score))
            print("PC hand contains {}".format(hand_list))
            return score


# pc_card_game()

def blackjackgame(player, pc):
    blackjack = 21

    if player > blackjack:
        print('Player over scored with points')
    elif player > pc and (player <= blackjack):
        print("player won!!!")
    elif player == pc and not (pc and player > blackjack):
        print("ITS A TIE :3")
    elif player < pc and not (pc > blackjack):
        print("PC WON")
    elif player > blackjack or player < pc and pc >= blackjack :
        print('player lost')


blackjackgame(user_card_game(), pc_card_game())
