def sum(a: float,b: float):
    #DocString
    """Sum of two variables.

    It receives two parameters, which it
    returns the Sum of this

    Args:
        a (float): Fist value  to be added
        b (float): Second value to be added

    Returns:
        float: Returns the Sum of two numbers
    """
    print("----")
    print("sum {} + {}".format(a,b))
    return print(a+b)

def diff(a: float,b: float):
    #DocString
    """Difference of two variables.

    It receives two parameters, which it
    returns the Difference of this

    Args:
        a (float): Fist value  to be added
        b (float): Second value to be added

    Returns:
        float: Returns the Difference of two numbers 
    """
    print("----")
    print("diff {} - {}".format(a,b))
    return print(a-b)

def mult(a: float,b: float):
    #DocString
    """Multiplication of two variables.

    It receives two parameters, which it
    returns the Multiplication of this

    Args:
        a (float): Fist value  to be added
        b (float): Second value to be added

    Returns:
        float: Returns the Multiplication of two numbers
    """
    print("----")
    print("mult {} * {}".format(a,b))
    return print(a*b)

def div(a: float,b: float):
    #DocString
    """Division of two variables.

    It receives two parameters, which it
    returns the Division of this

    Args:
        a (float): Fist value  to be added
        b (float): Second value to be added

    Returns:
        float: Returns the Division of two numbers
    """
    print("----")
    print("div {} / {}".format(a,b))
    return print(a / b)

def pow(a: float,b: float):
    #DocString
    """Pow of two variables.

    It receives two parameters, which it
    returns the Pow of this

    Args:
        a (float): Fist value  to be added
        b (float): Second value to be added

    Returns:
        float: Returns the Pow of two numbers
    """
    print("----")
    print("pow {} ^ {}".format(a,b))
    return print(a ** b)

def main():

    try:
        a=float(input("First Value > "))
        b=float(input("Second Value > "))

        sum(a,b)
        diff(a,b)
        mult(a,b)
        div(a,b)
        pow(a,b)
        
    except ZeroDivisionError as e:
        print("\n Error Division by cero:", e)
    except KeyboardInterrupt as error :
        print("\n CTRL-C pressed , thanks for executing getting_started_1.py script")
    except:
        print("\n Error catched, please try again")

if __name__ == "__main__":
    main()