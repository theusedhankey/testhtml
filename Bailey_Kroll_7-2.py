import random
GETITEMS = "wizard_all_items.txt"
STOREITEMS = "current_grabbed_items"

def wizard_menu():
    print("The Wizard Inventory Program\n"
          + "\nCOMMAND MENU"
          + "\nwalk - Walk down the path"
          + "\nshow - Show all items"
          + "\ndrop - Drop an item"
          + "\nexit - Exit program")


def read_items():
    total_items = []
    with open(GETITEMS) as file:
        for line in file:
            line = line.replace("\n", "")
            total_items.append(line)
        return total_items


def write_item(inventory,current_inventory):
    current_items = []
    number = random.randint(-1, len(inventory) - 1)
    item = inventory[number]
    choice = input("While walking down a path, you see a " + item + "."
                   + "\nDo you want to grab it? (y/n): ")
    if choice.lower() == "y":
        if len(current_inventory) < 4:
            current_items.append(item)
            with open(STOREITEMS, "a") as store_file:
                for store_item in current_items:
                    store_file.write(store_item + "\n")
            print("You picked up a " + item)
            return current_items[0]
        else:
            print("You can't carry any more items. Drop something first.")
    elif choice.lower() == "n":
        print("You have chosen to not pick up " + item)


def list_item(current_inventory):
    if len(current_inventory) == 0:
        print("There are no items in inventory\n")
    else:
        with open(STOREITEMS) as store_file:
            i = 1
            for store_item in store_file:
                print(str(i) + ".",store_item, end="")
                i+=1

def drop_item(current_inventory):
    if len(current_inventory) == 0:
        print("There is nothing to drop")
    else:
        number = int(input("Number "))
        if number < 1 or number > len(current_inventory):
            print("Invalid item number\n")
        else:
            item = current_inventory.pop(number-1)
            print("You dropped a "+ str(item) + ".\n")
            with open(STOREITEMS, "w") as store_file:
                for store_item in current_inventory:
                    store_file.write(store_item + "\n")

def exit_program():
    print("Bye!")
    exit()

def main():
    open(STOREITEMS, "w").close() # Start with a blank file to r/w too if file already exists
    wizard_menu()
    inventory = read_items()
    current_inventory = []
    while True:
        command = input("\nCommand: ")
        if command.lower() == "walk":
            current_inventory.append(write_item(inventory,current_inventory))
        elif command.lower() == "show":
            list_item(current_inventory)
        elif command.lower() == "drop":
            drop_item(current_inventory)
        elif command.lower() == "exit":
            exit_program()


if __name__ == '__main__':
    main()
