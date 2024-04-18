# Patys sukurkite bent 5 skirtingas funkcijas ir jas išbandykite.

def get_odd(a: int) -> bool:
    return True if a % 2 != 0 else False


print(get_odd(3))


def count_symbols(a: str) -> int:
    counter = 0
    for i in a:
        counter += 1
    return counter


print(count_symbols("fajkshgkjahsg asgjhajsg hajsgh"))
