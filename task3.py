# Sukurkite mini python programą, kuri kaip įvestį paimtų du skaičius ir grąžintų jų sumą, atimtį, dalybą, daugybą.



def calculator(x: int | float, y: int | float, z: str = "") -> str | float:
    # if z is None:
    #     return (f"Sum of numbers is {x + y}\nDiference of numbers is {x-y}\nMultiplying of numbers is {x*y}\n"
    #             f"Divide of numbers is {x/y}")
    if z == "+":
        return x + y
    elif z == "-":
        return x - y
    elif z == "*":
        return x * y
    elif z == "/":
        return x / y
    else:
        return (f"Sum of numbers is {x + y}\nDiference of numbers is {x - y}\nMultiplication of numbers is {x * y}\n"
                f"Division of numbers is {x / y}")


print(calculator(3, 12, "+"))
