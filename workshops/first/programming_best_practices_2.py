import random
import time

def timer(func):
    """
    A decorator function to measure the execution time of a function.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function.
    """
    def wrapper(*args, **kwargs):
        """
        The wrapper function that measures the execution time and prints it.

        Args:
            *args: Positional arguments passed to the decorated function.
            **kwargs: Keyword arguments passed to the decorated function.

        Returns:
            The result of the decorated function.
        """
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the decorated function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the execution time
        print(f"Execution time of {func.__name__}: {execution_time} seconds")
        return result

    return wrapper


@timer
def sort_and_print(numbers):
    """
    Sorts a list of numbers and prints the sorted numbers.

    Args:
        numbers (list): The list of numbers to be sorted.
    """
    sorted_numbers = sorted(numbers)  # Sort the numbers
    print(f"Sorted numbers: {sorted_numbers}")


def main():
    try:

        flag = False
        while not flag:
            print("-------")
            print("Welcome Main Menu")
            print("Time Execution test -> (1)")
            print("Exit -> (2)")
            user_input = input("Please choose a mode > ")

            if user_input == "1":  # Time Execution test

                max_num = int(input("Please enter the number maximum number you want to consider for the random sort test > "))
                n = int(input("Please enter the quantity of numbers you want for the random sort test > "))
                # Generate a list of random numbers
                random_numbers = [random.randint(1, max_num) for _ in range(n)]
                # Call the function decorated with timer
                sort_and_print(random_numbers)

            elif user_input == "2": #Exit
                flag = True

    except KeyboardInterrupt as error :
        print("\n CTRL-C pressed , thanks for executing programming_best_practices_2.py script")
    except:
        print("\n Error catched, please try again")

    print("Exit, thanks for executing programming_best_practices_2.py script")

if __name__ == "__main__":
    main()