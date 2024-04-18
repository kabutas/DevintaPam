# Sukurkite funkciją, kuri grąžintų tik unikalius simbolius turinčias string reikšmes.
from typing import List

sentence = "123456 parduotuve pilis masinu telefonas aaaa b21231b"

# papildyti inputu!


def string_filter(a: str) -> bool:
    for i in a:
        if a.count(i) > 1:
            return False
    return True


def word_splitter(a: str) -> List:
    uniques = []
    splitted_words = a.split(" ")
    for i in splitted_words:
        if string_filter(i):
            uniques.append(i)
    return uniques



print(f"Žodžiai su unikaliais symboliais: {word_splitter(sentence)}")
