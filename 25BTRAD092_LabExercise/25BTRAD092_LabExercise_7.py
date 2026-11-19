contacts = []

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        if any(c["phone"] == phone for c in contacts):
            print("Contact already exists!")
        else:
            contacts.append({"name": name, "phone": phone, "email": email})
            print("Contact added successfully!")

    elif choice == "2":
        name = input("Enter name to search: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == name.lower():
                print("Contact Found:", contact)
                found = True

        if not found:
            print("Contact not found!")

    elif choice == "3":
        phone = input("Enter phone number to update: ")
        found = False

        for contact in contacts:
            if contact["phone"] == phone:
                contact["name"] = input("Enter new name: ")
                contact["email"] = input("Enter new email: ")
                print("Contact updated successfully!")
                found = True
                break

        if not found:
            print("Contact not found!")

    elif choice == "4":
        phone = input("Enter phone number to delete: ")
        found = False

        for contact in contacts:
            if contact["phone"] == phone:
                contacts.remove(contact)
                print("Contact deleted successfully!")
                found = True
                break

        if not found:
            print("Contact not found!")

    elif choice == "5":
        if not contacts:
            print("Contact book is empty!")
        else:
            print("\n--- All Contacts ---")
            for contact in contacts:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("-------------------")

    elif choice == "6":
        print("Exiting Contact Book. Thank you!")
        break

    else:
        print("Invalid choice! Try again.")