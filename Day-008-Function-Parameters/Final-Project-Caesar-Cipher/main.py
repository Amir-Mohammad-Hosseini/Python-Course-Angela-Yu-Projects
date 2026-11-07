from art import logo

alphabet = ['a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y',
            'z']


def caesar(start_text, shift, direction):
    end_text = ""

    if direction == "decode":
        shift *= -1

    for char in start_text:
        if char in alphabet:
            alphabet_index = alphabet.index(char)
            shifted_index = (alphabet_index + shift) % len(alphabet)
            end_text += alphabet[shifted_index]

        else:
            end_text += char
    print(f"The {direction}d text is {end_text}")


print(logo)

should_continue = True

while should_continue:
    direction = input("Type 'encode'to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n") . lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

    again_choice = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.")
    if (again_choice != "yes"):
        should_continue = False
        print("Good bye!")
