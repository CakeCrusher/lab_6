"""
Sebastian repo: https://github.com/dev-par/lab6
Devan repo: https://github.com/CakeCrusher/lab_6
Name: Sebastian Sosa
"""

def encode(password: str):
    # increase the value of each digit in the password by 3
    newPass = ''
    for i in range(len(password)):
        newPass += str(int(password[i]) + 3)
    return newPass

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
            # CONTRIBUTOR PLEASE ADD DECODER HERE
            pass
        elif inp == "3":
            break

if __name__ == "__main__":
    main()