import random

list_letters = 'qwertyuiopasdfghjklzxcvbnm'
list_upper_letters = 'QWERTYUIOPLKJHGFDSAMNBVCXZ'
list_numbers = '1234567890'
list_special = '!@#$%^&*()_+'

BEGIN = 0

list_of_choices = []


# TODO in future this could be done better by future me, I would assume
#  this is quite hardcoded


def random_password_generator_v2():
    choice = ''
    while True:
        # here users entry gets split by ',' to get multiple choices
        user_input = input("Select options below which password should"
                           "contain, i.e. 1,2 or 1,3,4"
                           "\n1. Letters"
                           "\n2. Upper letters"
                           "\n3. Numbers"
                           "\n4. Special symbols"
                           "\n"
                           "\nYour choice: ").split(',')
        # for loop to append every choice of user into single list
        for choice in user_input:
            list_of_choices.append(choice)
        # below statement check's if user input is digits only and not
        # more then options in total if input actually has unnecessary
        # symbols loops is being exit and started again at the input part
        if choice not in '1234':
            print('-' * 100)
            print("Please try again use options from 1-4 and digits only")
            print('-' * 100)
            continue
        random_password = ''
        print('Type 0 for exit')
        # input for how many symbols a password should contain
        user_input = input("How many symbols should it have: ")
        # Exit condition
        if user_input == '0':
            break
        # random combination of lower case letters below
        if '1' in list_of_choices:
            for i in range(BEGIN, int(user_input)):
                generate = list_letters[random.randint(BEGIN, len(list_letters) - 1)]
                random_password += generate
        # random combination of upper case letters below
        if '2' in list_of_choices:
            for i in range(BEGIN, int(user_input)):
                generate = list_upper_letters[random.randint(BEGIN, len(list_upper_letters) - 1)]
                random_password += generate
        # random combination of numbers below
        if '3' in list_of_choices:
            for i in range(BEGIN, int(user_input)):
                generate = list_numbers[random.randint(BEGIN, len(list_numbers) - 1)]
                random_password += generate
        # random combination of special symbols below
        if '4' in list_of_choices:
            for i in range(BEGIN, int(user_input)):
                generate = list_special[random.randint(BEGIN, len(list_special) - 1)]
                random_password += generate
        # below combination of all choices that were made which is being randomized
        if user_input != '0':
            final_result = ''
            for i in range(BEGIN, int(user_input)):
                generate = random_password[random.randint(BEGIN, len(random_password) - 1)]
                final_result += generate
            print('-' * 100)
            print("Your new password is: {}".format(final_result))
            print('-' * 100)
            # Below line clears everything from list so new options can be selected
            list_of_choices.clear()


random_password_generator_v2()
