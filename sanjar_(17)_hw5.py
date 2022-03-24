contacts = [
    {'name': 'Geektech', 'phone': '0507052018'},
    {'name': 'Rescue Service', 'phone': '911'},
    {'name': 'Fire Service', 'phone': '101'},
]

def search(name):
    for i in contacts:
        if name == i['name']:
            return i
    print('не найден')
    return False

def contact_creat(name, phone):
    contacts.append({'name': name, 'phone': phone})

def contact_edit(name, phone):
    if search(name):
        new_name = input(f'New name ').upper()
        contacts[contacts.index(search(name))]['name'] = new_name
    elif search(phone):
        new_phone = input(f'new phone: ')
        contacts[contacts.index(search(phone))]['phone'] = new_phone
    else:
        print('не найден!')


def contact_delete(name):
    del contacts[contacts.index(search(name))]


def show_all():
    for i in contacts:
        print(i)


while 1:
    show_all()
    command = input(f'Выберите команду: \n'
                    '1) Create \n'
                    '2) Edit\n'
                    '3) Delete\n'
                    )
    name = input('name: ').title()
    phone = input('enter a number: ')
    if command == '1':
        contact_creat(name, phone)
    elif command == '2':
        contact_edit(name, phone)
    elif command == '3':
        contact_delete(name)
    elif command == 'q':
        print('Программа завершена! ')
    else:
        print("только от 1 до 3")




