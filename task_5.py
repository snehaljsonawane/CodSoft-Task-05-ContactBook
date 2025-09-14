contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("Contact added.")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        contacts[name] = phone
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

while True:
    print("\nOptions: add / search / update / delete / exit")
    choice = input("Choose: ").lower()

    if choice == 'add':
        add_contact()
    elif choice == 'search':
        search_contact()
    elif choice == 'update':
        update_contact()
    elif choice == 'delete':
        delete_contact()
    elif choice == 'exit':
        break
    else:
        print("Invalid option.")
