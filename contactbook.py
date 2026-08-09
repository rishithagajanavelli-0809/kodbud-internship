contacts = []

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)
        print("Contact added successfully!")

    elif choice == "2":
        if not contacts:
            print("No contacts found.")
        else:
            print("\n--- All Contacts ---")
            for contact in contacts:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("-------------------")

    elif choice == "3":
        search = input("Enter name to search: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == search.lower():
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                found = True

        if not found:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to delete: ")

        for contact in contacts:
            if contact["name"].lower() == name.lower():
                contacts.remove(contact)
                print("Contact deleted successfully!")
                break
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice!")