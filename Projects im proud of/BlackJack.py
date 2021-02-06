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


# TODO get correctly if statements on last function of blackjack game - DONE
#  write down/comment code
#  annotate/comment functions
#  make so that dictionary would represent actual deck and if on of the
#  cards was drawn if would have less chance of getting same again
#  put more code in functions if possible
#  fix value of king queen and jack which should be 10 and ace 1 or 11

# GAME RULES:
# All cards are at face value, except for the King, Queen and Jack which
# count as 10. An Ace will have a value of 11 unless that would give a
# player or the dealer a score in excess of 21; in which case, it has
# a value of 1. The dealer starts the game. Every player gets 2 cards, face up.


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
        # below if score of user is more than 21 player lost.
        if score > blackjack:
            print("Last card was {}".format(random_card))
            print("Total score was {}".format(score))
            # print("Better luck next time!")
            return score
        # in case score equal to 21 user is notified of getting 21
        elif score == blackjack:
            print("BlackJACK!")
            return score
        # once user gets a card he must decide to continue and draw
        # another card from deck or to stop and see what has PC drawn in his hand
        user_input = input("You got {}, total is now {} would you like "
                           "another one? (Y/N): ".format(random_card, score))
        if user_input == "y":
            continue
        if user_input == "n":
            return score


def pc_card_game():
    """
    Computer playing 21 and trying to get the score not above 21
    and not too low

    :return: score most appropriate for win
    """
    score = 0
    start_point = 0
    blackjack = 21
    hand_list = []
    while score <= blackjack:
        random_key = random.randint(start_point + 1, len(card_dict))
        score += random_key
        random_card = card_dict.get(random_key)
        hand_list.append(random_card)
        if blackjack >= score > 19:
            print("PC has got {}".format(score))
            print("PC hand contains {}".format(hand_list))
            print()
            return score
        if score > 21:
            print("Shitty score was {}".format(score))
            print("PC hand contains {}".format(hand_list))
            return score


while True:
    def blackjackgame(player, pc):
        blackjack = 21
        print(player)
        print(pc)
        if player > blackjack:
            print('Player over scored with points, therefore PC WON')
        elif player > pc and (player <= blackjack) or pc > blackjack > player:
            print('*' * 50)
            print("Player won!!!")
            print('*' * 50)
        elif player == pc and not (pc and player > blackjack):
            print('^' * 50)
            print("ITS A TIE :3")
            print('^' * 50)
        elif player < pc and not (pc > blackjack) or player > blackjack or player < pc:
            print('-' * 50)
            print("PC WON")
            print('-' * 50)
    user_input = input('Continue ? if yes hit any button, if no click 0')
    if user_input == '0':
        break

    blackjackgame(user_card_game(), pc_card_game())
