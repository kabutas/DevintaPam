# Write a program that defines a function called extract_email_addresses()
# that takes a text as input and extracts all email addresses from the text.


sentence = input("Enter text from where to extract Email addresses")

if not sentence:
    sentence = "123456 parduotuve pilis masinu telefonas aaaa b21231b bahjs@codeacademy.lt abkjbv@gmail.com"


def extract_email_addresses(a: str) -> list:
    email_list = []
    splitted_list = a.split(" ")
    for word in splitted_list:
        if "@" in word and "." in word:
            email_list.append(word)
    return email_list


print(extract_email_addresses(sentence))
