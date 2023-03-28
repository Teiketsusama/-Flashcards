import random

cards = {}


def add_card():
    print("The card:")
    while True:
        input_key = input()
        if input_key in cards.keys():
            print(f"The card \"{input_key}\" already exists. Try again:")
        else:
            break
    print("The definition of the card:")
    while True:
        input_value = input()
        if input_value in cards.values():
            print(f"The definition \"{input_value}\" already exists. Try again:")
        else:
            break
    cards[input_key] = input_value
    print(f"The pair (\"{input_key}\":\"{input_value}\") has been added.\n")


def remove_card():
    print("Which card?")
    input_key = input()
    if input_key in cards.keys():
        del cards[input_key]
        print("The card has been removed.\n")
    else:
        print(f"Can't remove \"{input_key}\": there is no such card.\n")


def import_cards():
    print("File name:")
    input_file = input()
    try:
        with open(input_file, "r") as file:
            for line in file:
                key, value = line.strip().split(":")
                cards[key] = value
        print(f"{len(cards)} cards have been loaded.\n")
    except FileNotFoundError:
        print("File not found.\n")


def export_cards():
    print("File name:")
    input_file = input()
    with open(input_file, "w") as file:
        for key, value in cards.items():
            file.write(f"{key}:{value}\n")
    print(f"{len(cards)} cards have been saved.\n")


def ask_cards():
    print("How many times to ask?")
    input_number = int(input())
    for i in range(input_number):
        random_card = random.choice(list(cards.keys()))
        print(f"Print the definition of \"{random_card}\":")
        input_value = input()
        if input_value == cards[random_card]:
            print("Correct!\n")
        elif input_value in cards.values():
            get_key = [key for key, value in cards.items() if value == input_value]
            print(f"Wrong. The right answer is \"{cards[random_card]}\", "
                  f"but your definition is correct for \"{get_key}\".\n")
        else:
            print(f"Wrong. The right answer is \"{cards[random_card]}\".\n")


def main():
    while True:
        user_input = input("Input the action (add, remove, import, export, ask, exit): \n")
        if user_input == "add":
            add_card()
        elif user_input == "remove":
            remove_card()
        elif user_input == "import":
            import_cards()
        elif user_input == "export":
            export_cards()
        elif user_input == "ask":
            ask_cards()
        elif user_input == "exit":
            print("Bye bye!")
            exit()


if __name__ == "__main__":
    main()
