# Patys sukurkite bent 5 skirtingas funkcijas ir jas išbandykite.
import random


# function to return true if number is odd
def get_odd(a: int) -> bool:
    return True if a % 2 != 0 else False


# function to count symbols in a string
def count_symbols(a: str) -> int:
    counter = 0
    for i in a:
        counter += 1
    return counter


# function to convert lower symbols to upper symbols
def convert_to_upper(word: str) -> str:
    return word.upper()


# function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 1.8 + 32


def get_random_number(a: int) -> int:
    return random.randint(0, a)


print(get_odd(3))
print(count_symbols("fajkshgkjahsg asgjhajsg hajsgh"))
print(convert_to_upper("text with uppercase"))
print(f"20 degrees by celsius equals to {celsius_to_fahrenheit(20)} by fahrenheit")
print(get_random_number(50))
