def string_reverse(string):
    """
    Recursively reverses a string.

    Args:
        string (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    if string:  # If the string has characters, reverse it
        return string[-1] + string_reverse(string[:-1])
    else:  # If the string is empty, return an empty string
        return ""

def main():
    try:

        flag = False
        while not flag:
            print("-------")
            print("Welcome Main Menu")
            print("Reverse String Method -> (1)")
            print("Exit -> (2)")
            user_input = input("Please choose a mode > ")

            if user_input == "1":  # Reverse your current string

                user_input_value = input("Please enter the string you want to reverse > ")

                print(f"For the original string {user_input_value} the reverse output is {string_reverse(user_input_value)}")

            elif user_input == "2": #Exit
                flag = True

    except KeyboardInterrupt as error :
        print("\n CTRL-C pressed , thanks for executing functions_datatypes_2.py script")
    except:
        print("\n Error catched, please try again")

    print("Exit, thanks for executing functions_datatypes_2.py script")

if __name__ == "__main__":
    main()