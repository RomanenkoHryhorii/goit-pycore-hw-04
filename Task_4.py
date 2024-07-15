def parse_input(user_input):
    """
    Розбирає введений користувачем рядок на команду та аргументи.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    """
    Додає новий контакт до словника контактів.
    """
    if len(args) != 2:
        return "Invalid number of arguments. Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """
    Змінює номер телефону для існуючого контакту.
    """
    if len(args) != 2:
        return "Invalid number of arguments. Usage: change [name] [new phone]"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    return "Contact not found."

def show_phone(args, contacts):
    """
    Показує номер телефону для вказаного контакту.
    """
    if len(args) != 1:
        return "Invalid number of arguments. Usage: phone [name]"
    name = args[0]
    if name in contacts:
        return contacts[name]
    return "Contact not found."

def show_all(contacts):
    """
    Показує всі збережені контакти.
    """
    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    """
    Головна функція програми, яка обробляє команди користувача.
    """
    contacts = {}  # Словник для зберігання контактів
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()