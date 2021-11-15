import re
my_text = 'Wasya, 1998, wasya@gmail.com'\
            'Wasy, 1998, wasy@gmail.com'\
            'Was, 1998, wa@gmail.com'\
            'Wa, 1998, w@gmail.com'\

searching = r"Wasya"
results = re.match(searching, my_text)
print(results)