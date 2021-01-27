import random
char_ref = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Reg Ex
def regex(check_these, letter):
    passed = True
    for x in check_these:
        if x == letter:
            passed = False
    return passed

# Encryption Function
def encrypt(shift, letter_char):
    if regex("!@#$%^&*()<>,.?/';:\"\| []\{\}`~1234567890+-_=", letter_char) == True:
        letter_char = letter_char.lower()
        letter_shifted_num = char_ref.index(letter_char) + shift
        if letter_shifted_num > 25:
            letter_shifted_num = letter_shifted_num - 26
        con_char = char_ref[letter_shifted_num]
        return con_char
    else:
        return letter_char


# Encryption User interface
def encrypt_ui():
    shift = int()
    print("What do you want the shift to be?(between 1-25)")
    shift = int(input())
    print("What is your message")
    message = input()
    coded_message = ""
    for char in message:
        coded_message += encrypt(shift, char)
    print("Your message is: " + str(coded_message))
    print("And the shift is: " + str(shift))

encrypt_ui()
