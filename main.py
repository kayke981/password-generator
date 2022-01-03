import random
import os

def change_yesOrno_to_bool(param):
    data = param.lower()
    # transforming 'yes' to 'true' and 'no' to 'false'
    if data == 'yes' or data == 'y':
        return True
    else:
        return False

def password_generator(leng, symbols, numbers):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    if symbols:
        abc = abc + '@!#$%&*_+=\|[{]}'
    if numbers:
        abc = abc + '1234567890'
    password_random = [random.choice(abc) for i in range(int(leng))]
    password = ''.join(password_random)
    return password

def main():
    # questions
    leng = input("How length of password?: ")
    symbols = input("Do you want symbols? [Y/N]: ")
    numbers = input("Do you want numbers? [Y/N]: ")
    print('[+] Generating password...')
    # password generator
    symbolBool = change_yesOrno_to_bool(symbols)
    numberBool = change_yesOrno_to_bool(numbers)
    password = password_generator(leng, symbolBool, numberBool)
    print(f'[+] Password generated: {password}')
    file = input(f'Do you want write the password ({password}) in a file? [Y/N]: ')
    fileBool = change_yesOrno_to_bool(file)
    # writing in a file
    if fileBool:
        print('[+] Writing...')
        with open('util/password.txt', 'a') as file:
            file.write(f'{password}\n')
        path = os.path.dirname(os.path.abspath(__file__))
        if "\\" in path:
            path = path + "\\util\password.txt"
        else:
            path = path + "/util/password.txt"
        print(f'[+] Wrote to {path}')
    print('[+] Done')
main()