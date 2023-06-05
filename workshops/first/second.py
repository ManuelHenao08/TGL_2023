from enum import Enum
NUMBER =""

class Temperature(Enum):
    CELSIUS = 1
    FAHRENHEIT = 2
    KELVIN = 3

class Conversion:
    def __init__(self, value:float , scale: Temperature) -> None:
        self.scale = scale
        self.value = value

        if self.scale == Temperature.CELSIUS:
            print("-------")
            print("Celsius conversion")
            conv1 = celsius_to_fahrenheit(value)
            print(f"celsius {value} °C to fahrenheit {conv1} °F")
            conv2 = celsius_to_kelvin(value)
            print(f"celsius {value} °C to kelvin {conv2} °K")

        if self.scale == Temperature.FAHRENHEIT:
            print("-------")
            print("Fahrenheit conversion")
            conv1 = fahrenheit_to_celsius(value)
            print(f"fahrenheit {value} °F to celsius {conv1} °F")
            conv2 = fahrenheit_to_kelvin(value)
            print(f"fahrenheit {value} °C to kelvin {conv2} °K")

        if self.scale == Temperature.KELVIN:
            print("-------")
            print("Kelvin conversion")
            conv1 = kelvin_to_celsius(value)
            print(f"kelvin {value} °K to celsius {conv1} °C")
            conv2 = kelvin_to_fahrenheit(value)
            print(f"kelvin {value} °K to fahrenheit {conv2} °F")

def celsius_to_fahrenheit(celsius:float):
    """
    Converts a temperature in Celsius to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The equivalent temperature in Fahrenheit.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit:float):
    """
    Converts a temperature in Fahrenheit to Celsius.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The equivalent temperature in Celsius.
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def celsius_to_kelvin(celsius:float):
    """
    Converts a temperature in Celsius to Kelvin.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The equivalent temperature in Kelvin.
    """
    kelvin = celsius + 273.15
    return kelvin


def kelvin_to_celsius(kelvin:float):
    """
    Converts a temperature in Kelvin to Celsius.

    Args:
        kelvin (float): The temperature in Kelvin.

    Returns:
        float: The equivalent temperature in Celsius.
    """
    celsius = kelvin - 273.15
    return celsius


def fahrenheit_to_kelvin(fahrenheit:float):
    """
    Converts a temperature in Fahrenheit to Kelvin.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The equivalent temperature in Kelvin.
    """
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = celsius_to_kelvin(celsius)
    return kelvin


def kelvin_to_fahrenheit(kelvin:float):
    """
    Converts a temperature in Kelvin to Fahrenheit.

    Args:
        kelvin (float): The temperature in Kelvin.

    Returns:
        float: The equivalent temperature in Fahrenheit.
    """
    celsius = kelvin_to_celsius(kelvin)
    fahrenheit = celsius_to_fahrenheit(celsius)
    return fahrenheit

def main():

    try:

        temperature_map = {
            "1": Temperature.CELSIUS,
            "2": Temperature.FAHRENHEIT,
            "3": Temperature.KELVIN
        }

        mode = False
        flag = False
        while not flag:
            print("-------")
            print("Welcome Main Menu")
            print("Temperature Conversion -> (1)")
            print("Exit -> (2)")
            user_input = input("Please choose a mode > ")

            if user_input == "1":  # Temperature Conversion
                while not mode:
                    print("-------")   
                    print("Choose choose the temperature scale from which you want to make conversions: ")
                    print("Celsius -> (1)")
                    print("Fahrenheit -> (2)")
                    print("Kelvin -> (3)")
                    user_input2 = input("Please temperature scale > ")
                    if user_input2 == "1" or  user_input2 == "2" or user_input2 == "3":
                        mode = True
                user_input_value = float(input("Please temperature scale value > "))
                temperature = temperature_map.get(user_input2, Temperature.FAHRENHEIT)
                conv = Conversion(user_input_value,temperature)
                mode=False

            elif user_input == "2": #Exit
                flag = True

    except KeyboardInterrupt as error :
        print("\n CTRL-C pressed , thanks for executing second.py script")
    except:
        print("\n Input Variables are not numbers, please try again")

    print("Exit, thanks for executing second.py script")


if __name__ == '__main__':
    main()