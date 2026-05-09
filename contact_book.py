import sys

class ContactBook:
    def __init__(self):
        """Initialize an empty contact book."""
        self.contacts = {}  

    def add_contact(self, name, phone, email, address):
        """Add a new contact. Name must be unique."""
        if name in self.contacts:
            print(f"\n❌ A contact with the name '{name}' already exists.")
            print("   Use 'update' to modify it, or choose a different name.\n")
            return False
        self.contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print(f"\n✅ Contact '{name}' added successfully!\n")
        return True

    def view_all_contacts(self):
        """Display all contacts with name and phone number."""
        if not self.contacts:
            print("\n📭 No contacts found.\n")
            return
        print("\n" + "=" * 50)
        print(f"{'Name':<20} {'Phone Number':<15}")
        print("=" * 50)
        for name, details in self.contacts.items():
            print(f"{name:<20} {details['phone']:<15}")
        print("=" * 50 + "\n")

    def search_contact(self, search_term):
        """Search for contacts by name or phone number (partial match)."""
        results = []
        search_term_lower = search_term.lower()
        for name, details in self.contacts.items():
            if (search_term_lower in name.lower()) or (search_term in details['phone']):
                results.append((name, details))
        if not results:
            print(f"\n🔍 No contacts found matching '{search_term}'.\n")
            return []
        print(f"\n🔎 Found {len(results)} contact(s) matching '{search_term}':")
        for name, details in results:
            print(f"\n  Name    : {name}")
            print(f"  Phone   : {details['phone']}")
            print(f"  Email   : {details['email']}")
            print(f"  Address : {details['address']}")
            print("-" * 30)
        return results

    def update_contact(self, name):
        """Update an existing contact's details."""
        if name not in self.contacts:
            print(f"\n❌ Contact '{name}' not found.\n")
            return False
        print(f"\n✏️  Updating contact: {name}")
        print("   Leave a field blank to keep the current value.\n")
        current = self.contacts[name]
        new_phone = input(f"   Phone ({current['phone']}): ").strip()
        new_email = input(f"   Email ({current['email']}): ").strip()
        new_address = input(f"   Address ({current['address']}): ").strip()

        if new_phone:
            current['phone'] = new_phone
        if new_email:
            current['email'] = new_email
        if new_address:
            current['address'] = new_address

        print(f"\n✅ Contact '{name}' updated successfully!\n")
        return True

    def delete_contact(self, name):
        """Delete a contact by name."""
        if name not in self.contacts:
            print(f"\n❌ Contact '{name}' not found.\n")
            return False
        del self.contacts[name]
        print(f"\n🗑️  Contact '{name}' deleted successfully!\n")
        return True

def main():
    """Main menu-driven interface."""
    book = ContactBook()
    
    while True:
        print("\n" + "=" * 50)
        print("           📒 CONTACT BOOK MENU")
        print("=" * 50)
        print("  1. Add Contact")
        print("  2. View All Contacts")
        print("  3. Search Contact")
        print("  4. Update Contact")
        print("  5. Delete Contact")
        print("  6. Exit")
        print("=" * 50)
        
        choice = input("  Enter your choice (1-6): ").strip()
        
        if choice == '1':
            print("\n--- Add New Contact ---")
            name = input("  Name: ").strip()
            if not name:
                print("  ❌ Name cannot be empty.\n")
                continue
            phone = input("  Phone number: ").strip()
            email = input("  Email: ").strip()
            address = input("  Address: ").strip()
            book.add_contact(name, phone, email, address)
        
        elif choice == '2':
            book.view_all_contacts()
        
        elif choice == '3':
            print("\n--- Search Contact ---")
            term = input("  Enter name or phone number to search: ").strip()
            if term:
                book.search_contact(term)
            else:
                print("  ❌ Search term cannot be empty.\n")
        
        elif choice == '4':
            print("\n--- Update Contact ---")
            name = input("  Enter the name of the contact to update: ").strip()
            if name:
                book.update_contact(name)
            else:
                print("  ❌ Name cannot be empty.\n")
        
        elif choice == '5':
            print("\n--- Delete Contact ---")
            name = input("  Enter the name of the contact to delete: ").strip()
            if name:
                confirm = input(f"  Are you sure you want to delete '{name}'? (y/n): ").strip().lower()
                if confirm in ['y', 'yes']:
                    book.delete_contact(name)
                else:
                    print("  Deletion cancelled.\n")
            else:
                print("  ❌ Name cannot be empty.\n")
        
        elif choice == '6':
            print("\n👋 Exiting Contact Book. Goodbye!\n")
            sys.exit(0)
        
        else:
            print("\n❌ Invalid choice. Please enter a number from 1 to 6.\n")

if __name__ == "__main__":
    main()
