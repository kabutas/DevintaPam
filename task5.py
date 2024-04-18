# Write a program that defines a function called extract_email_addresses()
# that takes a text as input and extracts all email addresses from the text.
from typing import List

sentence = "123456 parduotuve pilis masinu telefonas aaaa b21231b bahjs@codeacademy.lt abkjbv@gmail.com"


def email_extractor(a: str) -> List:
    email_list = []
    splitted_list = a.split(" ")
    for word in splitted_list:
        if "@" in word and "." in word:
            email_list.append(word)
    return email_list


print(email_extractor(sentence))
