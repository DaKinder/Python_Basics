import os

# shows all contacts in file
def show_contacts(myBook):
    os.system('cls')
    with open(myBook, 'r', encoding= 'utf-16') as file:
        data = file.readlines()
        # print(*data)

        for contact in data:
            print(contact, end='')
    input('\n\nPress any key')

# adds a new contact to file
def add_contact(myBook):
    os.system('cls')
    with open(myBook, 'a', encoding= 'utf-16') as file:
        res = ''
        res += input('Surname: ') + ' '
        res += input('Name: ') + ' '
        res += input("Father's name: ") + ' +7'
        res += input('Phone number: +7')

        file.write('\n' + res)

    input('OK! Press anykey')

# searches any contact
def find_contact(myBook):
    os.system('cls')
    target = input('Search: ')

    with open(myBook, 'r', encoding= 'utf-16') as file:
        data = file.read()
        contacts = file.readlines()

        if target in data:
            print('searching...')
            for line in contacts:
                if target in line:
                    print(line)
                    break
        else:
            print('No contact')
    input('Press anykey')

def drawing():
    print('1 - show contacts')
    print('2 - add contact')
    print('3 - find contact')
    print('4 - exit')

def main(path):
    
    while True:
        os.system('cls')
        drawing()
        user_input = int(input('make a chooce: '))

        if user_input == 1:
            show_contacts(path)
        elif user_input == 2:
            add_contact(path)
        elif user_input == 3:
            find_contact(path)
        elif user_input == 4:
            print('Finish')
            return
        