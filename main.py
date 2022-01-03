import random

def change_yesOrno_to_bool(param):
    data = param.lower()
    # transforming 'yes' to 'true' and 'no' to 'false'
    if data == 'yes' or data == 'y':
        return 'true'
    else:
        return 'false'

def password_generator(leng, symbols, numbers):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    if symbols.lower() == 'true':
        abc = abc + '@!#$%¨&*()_+=§-\|,.<>;:~^´`[{]}'
    if numbers.lower() == 'true':
        abc = abc + '1234567890'
    password_random = [random.choice(abc) for i in range(int(leng))]
    password = ''.join(password_random)
    return password

def main():
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
    if fileBool == 'true':
        print('[+] Writing to password.txt...')
        with open('password.txt', 'a') as file:
            file.write(f'{password}\n')
            print('[+] Wrote')
    print('[+] Done')
main()