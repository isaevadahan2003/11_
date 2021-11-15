contacts = [
    {'name': 'Geektech', 'phone': '0507052018'},
    {'name': 'Служба спасения', 'phone': '911'},
    {'name': 'Пожарная служба', 'phone': '101'},
]
def create(name, phone):
    contains = False
    for i in contacts:
        if i['name'] == name or i['phone'] == phone:
            contains = True
            break
    if contains:
        print("Такой контакт уже есть!")
    else:
        contacts.append({"name": name, 'phone': phone})

create("isaev", "0707770999")

def edit(name):
    iniContact = False
    for i in contacts:
        if i['name'] == name:
            iniContact = True
            break
    if iniContact:
            print('Такой номер уже есть!')
    else:
        print("Такого имени в контакте нет!")

edit('Geektech')

def delete(name):
    inContact = False
    for i in contacts:
        if i['name'] == name:
            inContact = True
            contacts.remove(i)
    if not inContact:
        print("Нельзя удалить то чего нет")

delete("Geektech")

def showContacts():
    print("\nСписок контактов:\n")
    for i in contacts:
        print(*i.values())

showContacts()



############################################################

# contacts = [
#     {
#         'name': 'coco-cola',
#         'phone': '0700700700'
#     },
#     {
#         'name': 'fanta',
#         'phone': '0700700700'
#     },
#     {
#         'name': 'sultan-chai',
#         'phone': '0700700700'
#     },
# ]
#
#
# def show_all_contact(lst):
#     for i in lst:
#         print(*i.values())
#
#
# def add_number(lst):
#     show_all_contact(contacts)
#     for i in lst:
#         name = input('Enter name: ')
#         phone = input('Enter phone: ')
#         n = dict(name=name.title(), phone=phone)
#         lst.append(n)
#         if i['phone'] == phone:
#             print("It's number repeat\n"
#                   "Please write wrong!")
#         elif i['name'] == name:
#             print("It's number repeat\n"
#                   "Please write wrong!")
#         else:
#             show_all_contact(contacts)
#             break
#
# def edit_name(lst):
#     show_all_contact(contacts)
#     name = input('Введите имя для изминения:')
#     for i in lst:
#         if i['name'] == name:
#             n = input('Введите имя:')
#             phone = input('Введите номер:')
#             i['name'] = name
#             if i['name'] == n:
#                 print("Номер повторяется!\n"
#                       "Пожалуйста напишите неправильно!")
#             if i['phone'] == phone:
#                 print("Номер повторяется!\n"
#                       "Пожалуйста напишите неправильно!")
#             else:
#                 i['name'] = n
#                 i['phone'] = phone
#                 show_all_contact(contacts)
#                 break
#
# def delete_contact(lst):
#     show_all_contact(contacts)
#     name = input('Введите имя для удаления: ')
#     for i in lst:
#         if i['name'] == name:
#             lst.remove(i)
#             break
#
#
# def searching_contact(lst):
#     show_all_contact(contacts)
#     name = input('Введите имя для поиска:')
#     for i in lst:
#         if i['name'] == name:
#             print(i['name'])
#             print(i['phone'])