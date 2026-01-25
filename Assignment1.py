# Program Name: Assignment1.py
# Course: IT3883 / Section 01
# Student Name: Jaleelah Bachou 
# Assignment Number: Lab 1
# Due Date: 01/24/2026
# Purpose: 
# This program creates a text-based menu that allows a user to store text 
# in a buffer, clear the stored text, display the current buffer contents, 
# and exit the program.
# Resources Used:
# Class notes, personal practice and studying. 

def display_menu():
    print("\n====== TEXT BUFFER MENU ======")
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")


def main():
    saved_text = ""
    entry_total = 0

    # Infinite loop keeps the program running until exit
    while True:
        display_menu()
        user_choice = input("Choose an option (1-4): ").strip()

        if user_choice == "1":
            # Prompt user to enter text to add to the buffer
            new_input = input("Enter text to add: ").strip()

          
            if saved_text:
                saved_text += " " + new_input
            else:
                saved_text = new_input

            entry_total += 1
            print("Text successfully added to buffer.")

        elif user_choice == "2":
            saved_text = ""
            entry_total = 0
            print("Buffer cleared. All stored text removed.")

        elif user_choice == "3":
            print("\n----- BUFFER CONTENT -----")
            if saved_text:
                print(saved_text)
                print(f"(Entries added: {entry_total})")
            else:
                print("The buffer is currently empty.")

        elif user_choice == "4":
            print("Program exiting. Thanks for using the buffer!")
            break

        else:
            print("Invalid selection. Please choose a number from 1 to 4.")


if __name__ == "__main__":
    main()
