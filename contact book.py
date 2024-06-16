class ContactBook:
    def __init__(self):
        self.contacts = {}  # Dictionary to store contacts {name: {phone, email, address}}

    def add_contact(self, name, phone, email, address):
        if name in self.contacts:
            print(f"Contact with name '{name}' already exists.")
        else:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            print(f"Contact '{name}' added successfully.")

    def display_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("\nList of Contacts:")
            for name, details in self.contacts.items():
                print(f"Name: {name}")
                print(f"Phone: {details['phone']}")
                print(f"Email: {details['email']}")
                print(f"Address: {details['address']}")
                print("---------------------")

    def search_contact(self, keyword):
        results = []
        for name, details in self.contacts.items():
            if keyword.lower() in name.lower() or keyword in details['phone']:
                results.append((name, details))
        
        if results:
            print(f"\nSearch results for '{keyword}':")
            for result in results:
                print(f"Name: {result[0]}")
                print(f"Phone: {result[1]['phone']}")
                print(f"Email: {result[1]['email']}")
                print(f"Address: {result[1]['address']}")
                print("---------------------")
        else:
            print(f"No contacts found matching '{keyword}'.")

    def update_contact(self, name, phone=None, email=None, address=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact with name '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact with name '{name}' not found.")


# Main program to interact with ContactBook
def main():
    contact_book = ContactBook()
    
    while True:
        print("\n***** Contact Book Menu *****")
        print("1. Add a new contact")
        print("2. Display all contacts")
        print("3. Search for a contact")
        print("4. Update a contact")
        print("5. Delete a contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        
        elif choice == '2':
            contact_book.display_contacts()
        
        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            contact_book.search_contact(keyword)
        
        elif choice == '4':
            name = input("Enter name of contact to update: ")
            phone = input("Enter new phone number (leave blank to keep existing): ").strip()
            email = input("Enter new email address (leave blank to keep existing): ").strip()
            address = input("Enter new address (leave blank to keep existing): ").strip()
            contact_book.update_contact(name, phone, email, address)
        
        elif choice == '5':
            name = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name)
        
        elif choice == '6':
            print("Exiting Contact Book.")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
