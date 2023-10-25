# Sebastian Sosa


def encode(password: str):
    # increase the value of each digit in the password by 3
    newPass = ''
    for i in range(len(password)):
        newPass += str(int(password[i]) + 3)
    return newPass


def decode(encoded_password):
    origPass = " "
    for i in range(len(encoded_password)):
        origPass += str((int(encoded_password[i]) - 3))
    return origPass

def main():
    encoded_password = ''
    while True:
        inp = input("""Menu
-------------
1. Encode
2. Decode
3. Quit

Please enter an option:""")
        if inp == "1":
            password = input("Please enter your password to encode:")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif inp == "2":
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}")

        elif inp == "3":
            break

if __name__ == "__main__":
    main()