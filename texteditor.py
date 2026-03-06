# Simple Text File Editor in Python

filename = input("Enter the file name (example: notes.txt): ")

while True:
    print("\n--- MENU ---")
    print("1. Create / Write file")
    print("2. View file")
    print("3. Edit (append text)")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        text = input("Enter text to write in file:\n")
        with open(filename, "w") as file:
            file.write(text)
        print("File saved successfully.")

    elif choice == "2":
        try:
            with open(filename, "r") as file:
                content = file.read()
                print("\n--- File Content ---")
                print(content)
        except FileNotFoundError:
            print("File does not exist.")

    elif choice == "3":
        text = input("Enter text to add:\n")
        with open(filename, "a") as file:
            file.write("\n" + text)
        print("Text added successfully.")

    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
