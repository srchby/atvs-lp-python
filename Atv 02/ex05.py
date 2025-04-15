import json
import re

contacts = []

def save_contacts():
    with open("contacts.json", "w") as outfile:
        json.dump(contacts, outfile, indent=4)
        
def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as infile:
            contacts = json.load(infile)
    except FileNotFoundError:
        contacts = []
    
def valid_number(number):
    pattern = r'^\(\d{2}\) \d{4,5}-\d{4}$'
    return re.match(pattern, number) is not None

def valid_email(email):
    return '@' in email and email.endswith('.com')
    
def add_contact(name, number, email):
    if not valid_email(email):
        print("Email não válido:")
        return
    if not valid_number(number):
        print("Número não válido:")
        return
    
    contacts.append({
        "name": name, 
        "number": number, 
        "email": email
        })
    
    save_contacts()
    
def search_contact(name):
    found = False
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            found = True
            print(f"\nContato encontrado: \nNome: {contact['name']} \nNúmero: {contact['number']} \nEmail: {contact['email']}")
    if not found:
        print("\nContato não encontrado")
    
def show_contacts():
    if not contacts:
        print("\nNenhum contato cadastrado")
        return
    
    print("\nContatos")
    for i, contact in enumerate(contacts, 1):
        print(f"\n{i}. \nNome: {contact['name']} \nNúmero: {contact['number']} \nEmail: {contact['email']}")
    

load_contacts()

while True:
    action = input("\n1. Adicionar contato \n2. Buscar contato \n3. Exibir contatos \n4. Sair \n>>")
    if action == "1":
        name = input("\nNome do contato: \n>> ").strip()
        number = input("\nNúmero do contato ((12) 12345-1234 ou (12) 1234-1234): \n>> ").strip()
        email = input("\nEmail do contato (abc@abc.com): \n>> ").strip()
        add_contact(name, number, email)
    elif action == "2":
        name = input("\nInsira nome do contato: \n>>")
        search_contact(name)
    elif action == "3":
        show_contacts()
    elif action == "4":
        save_contacts()
        break
    else:
        print("Ação inválida")