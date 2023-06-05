import unittest

def is_palindrome(word:str):
    """
    Checks if a word is a palindrome.

    Args:
        word (str): The word to check.

    Returns:
        bool: True if the word is a palindrome, False otherwise.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(word, str):
        raise TypeError("Input must be a string")

    cleaned_word = word.lower().replace(" ", "")  # Remove spaces and convert to lowercase
    reversed_word = cleaned_word[::-1]  # Reverse the word

    return cleaned_word == reversed_word


class TestIsPalindrome(unittest.TestCase):
    """
    Test cases for the is_palindrome function.
    """
    def test_palindrome(self):
        """
        Tests palindrome words.
        """
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_not_palindrome(self):
        """
        Tests non-palindrome words.
        """
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("Python"))

    def test_invalid_input(self):
        """
        Tests invalid input type.
        """
        with self.assertRaises(TypeError):
            is_palindrome(123)


def main():
    try:

        flag = False
        while not flag:
            print("-------")
            print("Welcome Main Menu")
            print("Palindrome words detector -> (1)")
            print("Exit -> (2)")
            user_input = input("Please choose a mode > ")

            if user_input == "1":  # Palindrome words detector

                user_input_value = input("Please enter the word you want to check if is palindrome > ")

                if is_palindrome(user_input_value): # Prime Number
                    print(f"The word '{user_input_value}' is a palindrome word")
                else: # Not Prime Number
                    print(f"The word '{user_input_value}' is not a palindrome word")

            elif user_input == "2": #Exit
                flag = True

    except KeyboardInterrupt as error :
        print("\n CTRL-C pressed , thanks for executing programming_best_practices_1.py script")
    except:
        print("\n Error catched, please try again")

    print("Exit, thanks for executing programming_best_practices_1.py script")

if __name__ == "__main__":
    #Run user test
    main()
    print("Run Unit Test: ")
    #Run Unit Test functions
    unittest.main()