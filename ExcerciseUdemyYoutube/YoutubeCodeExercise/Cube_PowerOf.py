# Fuctions exercise

def test_function_for_math():
    user_input = input("Would you like to have number CUBED(1) or raised to POWER(2) of: ")

    if user_input == "1":
        def cubed(cubed_choice=input("What number should be cubed: ")):
            result = int(cubed_choice) * int(cubed_choice) * int(cubed_choice)
            return result

        print(cubed())

    elif user_input == "2":

        def power(power_number=input("What should be power of: ")):
            result = int(power_number) * int(power_number)
            return int(result)

        print(power())


test_function_for_math()
