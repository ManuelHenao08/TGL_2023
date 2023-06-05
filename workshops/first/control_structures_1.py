def fib_loop(n:int):
    """
    Generates the Fibonacci sequence until the number value n given.

    Args:
        n (int): The number of terms in the Fibonacci sequence.

    Returns:
        list: The Fibonacci sequence.
    """
    sequence = []
    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence

def fib_recursive(n: int):
    """
    Recursive function to calculate the sum of Fibonacci number for a given term.

    Args:
        n (int): The term for which the Fibonacci number is calculated.

    Returns:
        int: The Sum of the Fibonacci sequence.
    """
    # Base case: if the term is 1 or 2, return 1
    if n == 1 or n == 2:
        return 1

    # Recursive case: calculate the Fibonacci number by summing the previous two terms
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def main():
    try:

        mode = False
        flag = False
        while not flag:
            print("-------")
            print("Welcome Main Menu")
            print("Fibonacci Sequence Generator -> (1)")
            print("Exit -> (2)")
            user_input = input("Please choose a mode > ")

            if user_input == "1":  # Fibonacci Sequence Generator
                while not mode:
                    print("-------")   
                    print("Choose the operation: ")
                    print("Fibonacci sequence -> (1)")
                    print("Sum of Fibonacci sequence -> (2)")
                    user_input2 = input("Please enter the method > ")
                    if user_input2 == "1" or  user_input2 == "2":
                        mode = True
                user_input_value = int(input("Please enter the number of terms in the Fibonacci sequence > "))
                if user_input2 == "1": #Recursive
                    print(f"Fibonacci sequence for n = {user_input_value} , the sequence is {fib_loop(user_input_value)}")
                elif user_input2 == "2": # Loop
                    print(f"Sum of Fibonacci sequence for n = {user_input_value} , the sequence is {fib_recursive(user_input_value)}")
                mode=False

            elif user_input == "2": #Exit
                flag = True

    except KeyboardInterrupt as error :
        print("\n CTRL-C pressed , thanks for executing control_structures_1.py script")
    except:
        print("\n Error catched, please try again")

    print("Exit, thanks for executing control_structures_1.py script")

if __name__ == "__main__":
    main()