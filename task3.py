# Sukurkite mini python programą, kuri kaip įvestį paimtų du skaičius ir grąžintų jų sumą, atimtį, dalybą, daugybą.
from typing import Union, Optional


def calculator(x: Union[int | float], y: Union[int | float], z: Optional[str] = "") -> str:
    # if z is None:
    #     return (f"Sum of numbers is {x + y}\nDiference of numbers is {x-y}\nMultiplying of numbers is {x*y}\n"
    #             f"Divide of numbers is {x/y}")
    if z == "+":
        return str(x + y)
    elif z == "-":
        return str(x - y)
    elif z == "*":
        return str(x * y)
    elif z == "/":
        return str(x / y)
    else:
        return (f"Sum of numbers is {x + y}\nDiference of numbers is {x - y}\nMultiplication of numbers is {x * y}\n"
                f"Division of numbers is {x / y}")


print(calculator(3, 12.5))
