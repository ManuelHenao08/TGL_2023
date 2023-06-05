def is_prime(number:int):
    """
    Checks if a number is prime.

    Args:
        number (int): The number to be checked.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def main():
    try:

        flag = False
        while not flag:
            print("-------")
            print("Welcome Main Menu")
            print("Prime number detector -> (1)")
            print("Exit -> (2)")
            user_input = input("Please choose a mode > ")

            if user_input == "1":  # Prime number detector

                user_input_value = int(input("Please enter the number you want to check if is prime > "))

                if is_prime(user_input_value): # Prime Number
                    print(f"The number {user_input_value} is a prime number")
                else: # Not Prime Number
                    print(f"The number {user_input_value} is a not a prime number")

            elif user_input == "2": #Exit
                flag = True

    except KeyboardInterrupt as error :
        print("\n CTRL-C pressed , thanks for executing control_structures_2.py script")
    except:
        print("\n Error catched, please try again")

    print("Exit, thanks for executing control_structures_2.py script")

if __name__ == "__main__":
    main()