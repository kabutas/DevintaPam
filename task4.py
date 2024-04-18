# Sukurkite funkciją, kuri grąžintų tik unikalius simbolius turinčias string reikšmes.
from typing import List

sentence = input("Enter text to filter words with unique characters only: ")

if not sentence:
    sentence = "123456 parduotuve pilis masinu telefonas aaaa b21231b bahjs@codeacademy.lt abkjbv@gmail.com"


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


print(f"Words with unique symbols only: {word_splitter(sentence)}")
