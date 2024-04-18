# Sukurkite mini python programą, kuri kaip įvestį paimtų du skaičius ir grąžintų jų sumą, atimtį, dalybą, daugybą.
from typing import Union, Optional


def calculator(x: Union[int | float], y: Union[int | float], z: Optional[str] = "+") -> float:
    if z == "+":
        return x + y
    elif z == "-":
        return x - y
    elif z == "*":
        return x * y
    elif z == "/":
        return x / y
    else:
        return -1


print(calculator(3, 12.5, "*"))
