# Contact Agenda Class
class ContactAgenda:
    def __init__(self):
        # Initialize the contact list as an empty dictionary
        self.contacts = {}

    def add_contact(self, name, phone, email):
        # Add a new contact to the agenda
        if name in self.contacts:
            print(f"Contact '{name}' already exists.")
        else:
            self.contacts[name] = {'phone': phone, 'email': email}
            print(f"Contact '{name}' added successfully.")

    def edit_contact(self, name, phone=None, email=None):
        # Edit an existing contact's details
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def remove_contact(self, name):
        # Remove a contact from the agenda
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' removed successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def search_contact(self, name):
        # Search for a contact by name
        if name in self.contacts:
            contact_info = self.contacts[name]
            print(f"Contact found: Name: {name}, Phone: {contact_info['phone']}, Email: {contact_info['email']}")
        else:
            print(f"Contact '{name}' not found.")

    def display_contacts(self):
        # Display all contacts in the agenda
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contacts List:")
            for name, info in self.contacts.items():
                print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

# Main function to interact with the user
def main():
    agenda = ContactAgenda()
    
    while True:
        print("\nContact Agenda Menu:")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Remove Contact")
        print("4. Search Contact")
        print("5. Display Contacts")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")
            agenda.add_contact(name, phone, email)
        
        elif choice == '2':
            name = input("Enter the name of the contact to edit: ")
            phone = input("Enter new phone (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            agenda.edit_contact(name, phone if phone else None, email if email else None)
        
        elif choice == '3':
            name = input("Enter the name of the contact to remove: ")
            agenda.remove_contact(name)
        
        elif choice == '4':
            name = input("Enter the name of the contact to search: ")
            agenda.search_contact(name)
        
        elif choice == '5':
            agenda.display_contacts()
        
        elif choice == '6':
            print("Exiting the Contact Agenda. Goodbye!")
            break
        
        else:
            print("Invalid option. Please choose a number between 1 and 6.")

# Run the main function
if __name__ == "__main__":
    main()