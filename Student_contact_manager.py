# Student Contact Manager

contacts = {}

# Sets to prevent duplicate emails and phone numbers
emails = set()
phones = set()


# Add Contact
def add_contact():
    contact_id = input("Enter Student ID or Email (Unique ID): ")

    if contact_id in contacts:
        print("❌ Contact already exists.")
        return

    name = input("Enter Full Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")
    role = input("Enter Role (Student/Parent/Teacher): ")

    # Validation
    if not name or not email or not phone or not role:
        print("❌ All fields are required.")
        return

    if email in emails:
        print("❌ This email is already being used.")
        return

    if phone in phones:
        print("❌ This phone number is already being used.")
        return

    contacts[contact_id] = {
        "name": name,
        "email": email,
        "phone": phone,
        "role": role
    }

    emails.add(email)
    phones.add(phone)

    print("✅ Contact added successfully.")


# Update Contact info
def update_contact():
    contact_id = input("Enter Contact ID to update: ")

    if contact_id not in contacts:
        print("❌ Contact not found.")
        return

    contact = contacts[contact_id]

    print("\nLeave blank to keep current value.")

    new_name = input(f"Name ({contact['name']}): ")
    new_email = input(f"Email ({contact['email']}): ")
    new_phone = input(f"Phone ({contact['phone']}): ")
    new_role = input(f"Role ({contact['role']}): ")

    # Update Email
    if new_email:
        if new_email != contact["email"] and new_email in emails:
            print("❌ Email already exists.")
            return

        emails.remove(contact["email"])
        emails.add(new_email)
        contact["email"] = new_email

    # Update Phone
    if new_phone:
        if new_phone != contact["phone"] and new_phone in phones:
            print("❌ Phone number already exists.")
            return

        phones.remove(contact["phone"])
        phones.add(new_phone)
        contact["phone"] = new_phone

    if new_name:
        contact["name"] = new_name

    if new_role:
        contact["role"] = new_role

    print("✅ Contact updated successfully.")


# Delete Contact
def delete_contact():
    contact_id = input("Enter Contact ID to delete: ")

    if contact_id not in contacts:
        print("❌ Contact not found.")
        return

    emails.remove(contacts[contact_id]["email"])
    phones.remove(contacts[contact_id]["phone"])

    del contacts[contact_id]

    print("✅ Contact deleted successfully.")


# Search Contact
def search_contact():
    contact_id = input("Enter Contact ID to search: ")

    if contact_id not in contacts:
        print("❌ Contact not found.")
        return

    contact = contacts[contact_id]

    print("\n--- Contact Details ---")
    print("Name :", contact["name"])
    print("Email:", contact["email"])
    print("Phone:", contact["phone"])
    print("Role :", contact["role"])


# List All Contacts
def list_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("\n===== ALL CONTACTS =====")

    for contact_id, details in contacts.items():
        print(f"\nID: {contact_id}")
        print(f"Name : {details['name']}")
        print(f"Email: {details['email']}")
        print(f"Phone: {details['phone']}")
        print(f"Role : {details['role']}")


# Main Menu
while True:
    print("\n===== STUDENT CONTACT MANAGER =====")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. List All Contacts")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        update_contact()

    elif choice == "3":
        delete_contact()

    elif choice == "4":
        search_contact()

    elif choice == "5":
        list_contacts()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please select 1-6.")