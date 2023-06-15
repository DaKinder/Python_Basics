def show_contacts(myBook):
    with open(myBook, 'r', encoding= 'utf-8') as file:
        data = file.readlines()
        print(*data)

