def count_word_occurrences(text):
    """
    Counts the occurrences of each word in a given text.

    Args:
        text (str): The input text.

    Returns:
        dict: A dictionary with word counts.
    """
    word_counts = {}  # Initialize an empty dictionary to store word counts

    # Split the input text into words
    words = text.strip().split()

    for word in words:
        # Increment the count for each word
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def main():
    try:
        numbers=[]
        mode = False
        flag = False
        while not flag:
            print("-------")
            print("Welcome Main Menu")
            print("Count Word Occurence -> (1)")
            print("Exit -> (2)")
            user_input = input("Please choose a mode > ")

            if user_input == "1":  # Count Word Occurence
                while not mode:
                    print("-------")   
                    print("Choose the operation: ")
                    print("Read from a text file -> (1)")
                    print("Read from user input -> (2)")
                    user_input2 = input("Please enter the method > ")
                    if user_input2 == "1" or  user_input2 == "2":
                        mode = True

                    if user_input2 =="1": #Read from a text file
                        file_path = 'sample_advanced_python_2.txt' 
                        with open(file_path, 'r') as file:
                            text = file.read()

                        word_counts = count_word_occurrences(text)
                        # Print the word counts
                        for word, count in word_counts.items():
                            print(f'{word}: {count}')

                    elif user_input2 == "2": #Read from user input
                        user_input = input("Enter some text: ")
                        word_counts = count_word_occurrences(user_input)

                        # Print the word counts
                        for word, count in word_counts.items():
                            print(f'{word}: {count}')       
                
                mode=False

            elif user_input == "2": #Exit
                flag = True

    except KeyboardInterrupt as error :
        print("\n CTRL-C pressed , thanks for executing advanced_python_2.py script")
    except:
        print("\n Error catched, please try again")

    print("Exit, thanks for executing advanced_python_2.py script")

if __name__ == "__main__":
    main()