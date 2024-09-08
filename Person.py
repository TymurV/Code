from pystyle import Colors, Colorate, Write
Person = {
    'Name': 'Tom', 
    'Years': 29,
    'Company': 'SuperCorp',
    'Programming_lang': ['JS', 'Python']
}

Person.update(Phone = 'Android')
for i in Person:
    Write.Print(f"{i}: {Person[i]}\n", Colors.yellow_to_red, interval=0.05)