def read_notes():
    with open("notes.txt", "r") as file:
        print("\nYour notes:")
        print("--------------------")
        print(file.read())

def add_note():
    with open("notes.txt", "a") as file:
        text = input("Write a note: ")
        file.write(text + "\n")

    print("\nNote saved successfully!\n")

def menu_selection():
    print("====================")
    print("Notes Manager")
    print("====================")
    print("1. Add a note")
    print("2. View all notes")
    print("3. Exit")

    selection = int(input("\nChoose an option: "))
    return selection

while True:

    selection = menu_selection()

    if selection == 1:
        add_note()
        read_notes()

    elif selection == 2:
        read_notes()

    elif selection == 3:
        print("\nThank you! Have a nice day!")
        break

    else:
        print("\nInvalid option. Please try again.\n")





