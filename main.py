from data_generator import *


def print_menu_options(menu):
    for m in menu.items():
        print(f"{m.keys}- {m.values}")


def main():
    print("Welcome to the Data Generator")
    menu_options = {"1": "Patient Data","2": "Practitioner Data", "3": "Appointment Data", "Q": "Quit"}
    print_menu_options(menu_options)


if __name__ == "__main__":
    main()