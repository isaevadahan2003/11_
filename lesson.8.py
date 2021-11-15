contacts = [
    {
        'name': 'coco-cola',
        'phone': '0700700700'
    },
    {
        'name': 'fanta',
        'phone': '0700700700'
    },
    {
        'name': 'sultan-chai',
        'phone': '0700700700'
    },
]

def show_all_contact(lst):
    for i in lst:
        print(*i.values())


def add_number(lst):
    show_all_contact(contacts)
    for i in lst:
        name = input('Enter name: ')
        phone = input('Enter phone: ')
        n = dict(name=name.title(), phone=phone)
        lst.append(n)
        if i['phone'] == phone:
            print("It's number repeat\n"
                  "Please write wrong!")
        elif i['name'] == name:
            print("It's number repeat\n"
                  "Please write wrong!")
        else:
            show_all_contact(contacts)
            break

def edit_name(lst):
    show_all_contact(contacts)
    name = input('Введите имя для изминения:')
    for i in lst:
        if i['name'] == name:
            n = input('Введите имя:')
            phone = input('Введите номер:')
            i['name'] = name
            if i['name'] == n:
                print("Номер повторяется!\n"
                      "Пожалуйста напишите неправильно!")
            if i['phone'] == phone:
                print("Номер повторяется!\n"
                      "Пожалуйста напишите неправильно!")
            else:
                i['name'] = n
                i['phone'] = phone
                show_all_contact(contacts)
                break

def delete_contact(lst):
    show_all_contact(contacts)
    name = input('Введите имя для удаления: ')
    for i in lst:
        if i['name'] == name:
            lst.remove(i)
            break


def searching_contact(lst):
    show_all_contact(contacts)
    name = input('Введите имя для поиска:')
    for i in lst:
        if i['name'] == name:
            print(i['name'])
            print(i['phone'])


while True:
    command = input("Enter what we'll do: add = 'a', search = 's' edit = 'e' or delete = 'd' or 'q' for quite")
    if command == 'a':
        add_number(contacts)
    elif command == 'e':
        edit_name(contacts)
    elif command == 's':
        searching_contact(contacts)
    elif command == 'd':
        delete_contact(contacts)
    elif command == 'f':
        print('Программа завершина!')
        break