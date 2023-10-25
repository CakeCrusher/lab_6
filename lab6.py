# def decode(password: str):
#     # decrease the value of each digit in the password by 3
#     newPass = ''
#     for i in range(len(password)):
#         newPass += str(int(password[i]) - 3)
#     return newPass
def encode(password: str):
    # increase the value of each digit in the password by 3
    newPass = ''
    for i in range(len(password)):
        newPass += str(int(password[i]) + 3)
    return newPass

def main():
    while True:
        inp = input("Enter a number 0 for decode 1 for encode: ")
        if inp == "0":
            # CONTRIBUTOR PLEASE ADD DECODER
            # password = input("Enter a password: ")
            # print(decode(password))
        elif inp == "1":
            password = input("Enter a password: ")
            print(encode(password))

if __name__ == "__main__":
    main()