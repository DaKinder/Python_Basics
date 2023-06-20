import os

# shows all contacts in file
def show_contacts(myBook):
    os.system('cls')
    with open(myBook, 'r', encoding='utf-16') as file:
        data = file.readlines()

        for contact in data:
            print(contact, end='')
    input('\n\nPress any key')

# adds a new contact to file
def add_contact(myBook):
    os.system('cls')
    with open(myBook, 'a', encoding='utf-16') as file:
        newContact = ''
        newContact += input('Surname: ') + ' '
        newContact += input('Name: ') + ' +7'
        newContact += input('Phone number: +7')

        file.write('\n' + newContact)

    input('OK! Press anykey')

# searches any contact
def find_contact(myBook):
    os.system('cls')
    request = input('Search: ')
    with open(myBook, 'r', encoding='utf-16') as file:
        contacts = file.readlines()
        
        for line in contacts:
            if request in line:
                print(i)
                print(line)
                break
        else:
            print('No contact')
    input('Press Enter')

# edits contact
def edit_contact(myBook): 
    os.system('CLS')
    with open(myBook, 'r', encoding='utf-16') as data:
        phone_book = data.read()
        print(phone_book)
        
        index_data = int(input('Input number of a line to correction: ')) -1
        phone_book_lines = phone_book.split('\n')
        edit_phone_book_lines = phone_book_lines[index_data]
        elements = edit_phone_book_lines.split('\n')
        surname = input('Input a surname: ')
        phone_number = input('Input a number: ')
        num = elements[0]
        
        if len(surname) == 0:
            surname = elements[1]
        
        if len(phone_number) == 0:
            phone_number = elements[2]
            
        edited_line = f'{num} {surname} {phone_number}' 
        phone_book_lines[index_data] = edited_line
        print(f'The line {edit_phone_book_lines} was correctly edited as {edited_line}\n')
        
        with open(myBook, 'w', encoding='utf-16') as f:
            f.write('\n'.join(phone_book_lines))
        
        
        

#deletes contact
def delete_contact(myBook):
    os.system('CLS')
    with open(myBook, 'r', encoding='utf-16') as data:
        phone_book = data.read()
        print(phone_book)
        
    index_data = int(input('Input number of line to delete: ')) -1
    phone_book_lines = phone_book.split('\n')
    del_phone_book_lines = phone_book_lines[index_data]
    phone_book_lines.pop(index_data)
    
    print(f'The record {del_phone_book_lines} was deleted\n')
    
    with open(myBook, 'w', encoding='utf-16') as data:
            data.write('\n'.join(phone_book_lines))


# draws the main UI
def drawing_main():
    print('1 - show contacts')
    print('2 - add contact')
    print('3 - find contact')
    print('4 - edit contact')
    print('5 - to delete')
    print('q - exit')

# draws the edit menu
def drawing_edit():
    print('Edit mode...')
    print('1 - for Surname')
    print('2 - for Name')
    print('4 - for Phone Number')
    print('0 - to cancel!!!')
    
#  program starts here
def main(path):

    while True:
        os.system('cls')
        drawing_main()
        user_input = int(input('make a chooce: '))

        if user_input == 1:
            show_contacts(path)
        elif user_input == 2:
            add_contact(path)
        elif user_input == 3:
            find_contact(path)
        elif user_input == 4:
            edit_contact(path)
        # elif user_input == 5:
            # delete_contact(path)
        elif user_input == 'q':
            print('Finish')
            return
