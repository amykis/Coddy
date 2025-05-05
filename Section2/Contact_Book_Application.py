def display_menu():
    print('''Contact Book Menu:
1. Add Contact
2. View Contact
3. Edit Contact
4. Delete Contact
5. List All Contacts
6. Exit''')


def add_contact(contact_book):
    name = input()
    phone = input()
    email = input()
    address = input()
    if name in contact_book:
        print("Contact already exists!")
    else:
        contact_book[name] = {"phone": phone, "email": email, "address": address}
        print("Contact added successfully!")


def view_contact(contact_book):
    name = input()
    if name in contact_book.keys():
        print(f"Name: {name}\nPhone: {contact_book[name]['phone']}\nEmail: {contact_book[name]['email']}\nAddress: {contact_book[name]['address']}")
    else:
        print("Contact not found!")


def edit_contact(contact_book):
    name = input()
    if name in contact_book.keys():
        phone = input()
        email = input()
        address = input()
        if len(phone) > 0:
            contact_book[name]['phone'] = phone
        if len(email) > 0:
            contact_book[name]['email'] = email
        if len(address) > 0:
            contact_book[name]['address'] = address
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def delete_contact(contact_book):
    name = input()
    if name in contact_book.keys():
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def list_all_contacts(contact_book):
    if len(contact_book) > 0:
        for name in contact_book.keys():
            print(f"Name: {name}\nPhone: {contact_book[name]['phone']}\nEmail: {contact_book[name]['email']}\nAddress: {contact_book[name]['address']}\n")
    else:
        print("No contacts available.")

contact_book = {}

while True:
    display_menu()
    using = int(input())
    if using == 1:
        add_contact(contact_book)
    elif using == 2:
        view_contact(contact_book)
    elif using == 3:
        edit_contact(contact_book)
    elif using == 4:
        delete_contact(contact_book)
    elif using == 5:
        list_all_contacts(contact_book)
    elif using == 6:
        break