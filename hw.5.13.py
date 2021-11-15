contacts = [
    {'name': 'Geektech', 'phone': '0507052018'},
    {'name': 'Служба спасения', 'phone': '911'},
    {'name': 'Пожарная служба', 'phone': '101'},
]
def create(name, phone):
    contains = False
    for i in contacts:
        if (i['name'] == name or i['phone'] == phone):
            contains = True
            break
    if (contains):
        print("Такой контакт уже есть!")
    else:
        contacts.append({"name": name, 'phone': phone})

create("isaev", "0707770999")

def edit(name, phone):
    inContact = False
    for i in contacts:
        if (i['name'] == name):
            inContact = True

            i['phone'] = phone
            break
    if (not inContact):
        print("Такого имени в контакте нет!")

edit('Geektech', '0507052018')

def delete(name):
    inContact = False
    for i in contacts:
        if(i['name']==name):
            inContact = True
            contacts.remove(i)
    if(not inContact):
        print("Нельзя удалить то чего нет")

delete("Geektech")

def showContacts():
    print()
    print("Список контактов")
    print()
    for i in contacts:
        print(*i.values())

showContacts()
