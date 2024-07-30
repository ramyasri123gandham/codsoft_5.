''' Contact Book  
Contact Information: Store name, phone number, email, and address for each contact.
 Add Contact: Allow users to add new contacts with their details.
 View Contact List: Display a list of all saved contacts with names and phone numbers.
 Search Contact: Implement a search function to find contacts by name or phone number.
 Update Contact: Enable users to update contact details.
 Delete Contact: Provide an option to delete a contact.
 User Interface: Design a user-friendly interface for easy interaction.'''


class Contacts:
    def __init__(self):
        self.contact_list = []

    def add_contact(self, name, mob_no, email, address):
        self.contact_list.append({'name': name, 'mob_no': mob_no, 'email': email, 'address': address})
        print(f"{name} has been added to your contacts.")

    def view_contacts(self):
        if not self.contact_list:
            print("No contacts available.")
            return
        for i, contact in enumerate(self.contact_list):
            print(f"{i + 1}. Name: {contact['name']}, Phone: {contact['mob_no']}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contact_list if search_term.lower() in contact['name'].lower() or search_term in contact['mob_no']]
        if results:
            for contact in results:
                print(f"Name: {contact['name']}, Phone: {contact['mob_no']}, Email: {contact['email']}, Address: {contact['address']}")
        else:
            print("No contact found with that name or phone number.")

    def update_contact(self, search_term):
        for contact in self.contact_list:
            if search_term.lower() in contact['name'].lower() or search_term in contact['mob_no']:
                print(f"Found contact: Name: {contact['name']}, Phone: {contact['mob_no']}, Email: {contact['email']}, Address: {contact['address']}")
                name = input("Enter new name (leave blank to keep current): ") or contact['name']
                mob_no = input("Enter new phone number (leave blank to keep current): ") or contact['mob_no']
                email = input("Enter new email (leave blank to keep current): ") or contact['email']
                address = input("Enter new address (leave blank to keep current): ") or contact['address']
                contact.update({'name': name, 'mob_no': mob_no, 'email': email, 'address': address})
                print("Contact updated successfully.")
                return
        print("No contact found with that name or phone number.")

    def delete_contact(self, search_term):
        for contact in self.contact_list:
            if search_term.lower() in contact['name'].lower() or search_term in contact['mob_no']:
                self.contact_list.remove(contact)
                print("Contact deleted successfully.")
                return
        print("No contact found with that name or phone number.")

def main():
    contacts = Contacts()
    
    print("\nContact Book Menu:")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")

    while True:
               
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            mob_no = input("Enter mobile number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contacts.add_contact(name, mob_no, email, address)
        elif choice == '2':
            contacts.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contacts.search_contact(search_term)
        elif choice == '4':
            search_term = input("Enter name or phone number to update: ")
            contacts.update_contact(search_term)
        elif choice == '5':
            search_term = input("Enter name or phone number to delete: ")
            contacts.delete_contact(search_term)
        elif choice == '6':
            print("Exiting the contact book application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
