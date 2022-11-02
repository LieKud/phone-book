from ast import While
from traceback import print_list




#UZDEVUMS:
#izveido izvēlni lai lietotājs var izvēlēties ko darīs:
#1. Ivadīt jaunu kontaktu
#2. Izvadīt kontaktus
#3. Pārtraukt darbības un iziet no programmas
contacts = []

while(True):
    response = input('(1)add contact (2)print contacts (3)exit:   ')
    if response == '1':
        person_name = input('Name: ')
        person_surname = input('Surname: ')
        person_phone = input('Phone: ')
        person_email = input('Email: ')

        person_contact = {
            'name': person_name,
            'surname': person_surname,
            'phone': person_phone,
            'email': person_email
        }

        contacts.append(person_contact)
    elif response == '2':
           print("---Contact---")
    for i in range(len(contacts)):
    print(contacts[i]["name"],end=" ")
    print(contacts[i]["surname"]) 
    print(contacts[i]["phone"])
    print(contacts[i]["email"])
    elif response == '3':
    print('Bye bye!')
        exit()
    else:
        print("Please choose 1/2/3")

    

