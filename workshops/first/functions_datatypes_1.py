def find_maximum(numbers:list):
    """
    Finds the maximum value in a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        int or float: The maximum value in the list.

    Raises:
        ValueError: If the input list is empty.
    """
    if len(numbers) == 0:
        raise ValueError("Input list cannot be empty")

    maximum = numbers[0]  # Initialize maximum with the first element

    for num in numbers:
        if num > maximum:
            maximum = num

    return maximum


def main():
    try:
        numbers=[]
        flag = False
        while not flag:
            print("-------")
            print("Welcome Main Menu")
            print("Find the maximun number on a list -> (1)")
            print("Exit -> (2)")
            user_input = input("Please choose a mode > ")

            if user_input == "1":  # Find the maximun number on a list
                
                while True:
                    try:
                        user_input = input("Enter a number (or 'x' to finish): ")
                        
                        if user_input.lower() == 'x':
                            break
                        
                        number = float(user_input)
                        numbers.append(number)
                    
                    except ValueError:
                        print("Invalid input! Please enter a valid number or 'x' to finish.")

                print(f"For the list {numbers} the maximum value is {find_maximum(numbers)}")

            elif user_input == "2": #Exit
                flag = True

    except KeyboardInterrupt as error :
        print("\n CTRL-C pressed , thanks for executing functions_datatypes_1.py script")
    except:
        print("\n Error catched, please try again")

    print("Exit, thanks for executing functions_datatypes_1.py script")

if __name__ == "__main__":
    main()