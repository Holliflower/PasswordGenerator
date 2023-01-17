import random


# A function do shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)


uppercaseLetter1 = chr(random.randint(65, 90))  # Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2 = chr(random.randint(65, 90))  # Generate a random Uppercase letter (based on ASCII code)

lowercaseLetter1 = chr(random.randint(97, 122))  # Generate a random Lowercase letter (based on ASCII code)
lowercaseLetter2 = chr(random.randint(97, 122))  # Generate a random Lowercase letter (based on ASCII code)

digit1 = chr(random.randint(48, 57))  # Generate a random number between 0-9 (based on ASCII code)
digit2 = chr(random.randint(48, 57))  # Generate a random number between 0-9 (based on ASCII code)


specialcharacter1 = chr(random.randint(33, 47))  # Generate a random punctuation (based on ASCII code)
specialcharacter2 = chr(random.randint(33, 47))  # Generate a random punctuation (based on ASCII code)

# Generate random password from above random generated characters.
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2\
           + specialcharacter1 + specialcharacter2

password = shuffle(password)

# Output
print(password)
