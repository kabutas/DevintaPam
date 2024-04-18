# Sukurkite funkciją, kuri prie kiekvieno list nario prideda string galūnę.


def add_string_ending(input_list: list) -> list:
    modded_list = []
    for i in input_list:
        if i[-1] == "1":
            if i == "11":
                modded_list.append(i + "-th")
            else:
                modded_list.append(i + "-st")
        elif i[-1] == "2":
            if i == "12":
                modded_list.append(i + "-th")
            else:
                modded_list.append(i + "-nd")
        elif i[-1] == "3":
            if i == "13":
                modded_list.append(i + "-th")
            else:
                modded_list.append(i + "-rd")
        else:
            modded_list.append(i + "-th")

    return modded_list


print(add_string_ending(["1", "3", "8", "11", "22", "21", "31", "41", "215"]))
