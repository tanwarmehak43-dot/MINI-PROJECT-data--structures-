contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View Contacts")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        number = input("Enter number: ")
        contacts[name] = number
        print("Contact added!")

    elif choice == 2:
        name = input("Enter name to search: ")
        print("Number:", contacts.get(name, "Not found"))

    elif choice == 3:
        name = input("Enter name to delete: ")
        contacts.pop(name, None)
        print("Deleted!")

    elif choice == 4:
        print(contacts)

    elif choice == 5:
        break