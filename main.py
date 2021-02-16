char_ref = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Regular Expresion
def regex(check_these, letter):
    passed = True
    for x in check_these:
        if x == letter:
            passed = False
    return passed


# Encryption/Decryption backend class
class endec:
    # Encryption
    def encrypt(shift, letter_char):
        upper = False
        # Check to eliminate all non alphabetic charicters and pass them imdediatly back
        if regex("!@#$%^&*()<>,.?/';:\"\| []\{\}`~1234567890+-_=", letter_char) == True:
            # Check if it is upper case
            if letter_char.isupper() == True:
                upper = True
            # Get the location of the letter in the array
            letter_shifted_num = char_ref.index(letter_char.lower()) + shift
            if letter_shifted_num > 25:
                letter_shifted_num = letter_shifted_num - 26
            con_char = char_ref[letter_shifted_num]
            # Pass back if the item is upper case or not
            if upper == True:
                return con_char.upper()
            else:
                return con_char
        else:
            return letter_char

    # Decryption
    def decryption(shift, letter_char):
        upper = False
        if regex("!@#$%^&*()<>,.?/';:\"\| []\{\}`~1234567890+-_=", letter_char) == True:
            if letter_char.isupper() == True:
                upper = True
            shift_num = char_ref.index(letter_char.lower()) - shift
            if upper == True:
                return char_ref[shift_num].upper()
            else:
                return char_ref[shift_num]
        else:
            return letter_char

# Create Abreviated class instance
en = endec
# Encryption User interface
def encrypt_ui():
    shift = int()
    print("What do you want the shift to be?(between 1-25)")
    shift = int(input())
    print("What is your message")
    message = input()
    coded_message = ""
    counter = 0
    for char in message:
        coded_message += en.encrypt(shift, char)
    print("Your message is: " + str(coded_message))
    print("And the shift is: " + str(shift))

# Decryption UI
def decrypt_ui():
    shift = int()
    print("What is the shift")
    shift = int(input())
    print("What is your message")
    message = input()
    coded_mesage = ""
    for chars in message:
        coded_mesage += en.decryption(shift, chars)
    print("Your message is: " + str(coded_mesage))

# Encryption and Decryption UI
def main():
    print("Would you like to:\n[1]Decrypt\n[2]Encrypt")
    choice1 = input()
    if choice1 == "1":
        decrypt_ui()
    elif choice1 == "2":
        encrypt_ui()
    else:
        main()

main()
