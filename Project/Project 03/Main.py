def add_item(inventory):
    """Asks the user for an item and adds it to the inventory list."""
    item = input("Enter an item to add to your inventory: ")
    if item:
        inventory.append(item)
        print(f"'{item}' has been added to your inventory.")
    else:
        print("Item name cannot be empty.")

def show_inventory(inventory):
    """Prints all contents of the inventory list."""
    if not inventory:
        print("Your inventory is currently empty.")
    else:
        print("\n--- Current Inventory ---")
        for index, item in enumerate(inventory, start=1):
            print(f"{index}. {item}")

def clear_inventory(inventory):
    """Clears all items from the inventory list."""
    if not inventory:
        print("Inventory is already empty.")
    else:
        inventory.clear()
        print("Your inventory has been cleared!")

def main():
    inventory = []
    
    while True:
        print("\n=== Main Menu ===")
        print("1. Add item to inventory")
        print("2. View inventory")
        print("3. Clear inventory")
        print("4. Exit game")
        
        choice = input("Select an option (1-4): ")
        
        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            show_inventory(inventory)
        elif choice == "3":
            clear_inventory(inventory)
        elif choice == "4":
            print("Exiting game. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
    