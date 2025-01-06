import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    # if decode, shift backwards
    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1

        if letter not in alphabet:
            output_text += letter
        else:
            # Shift to get the output
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


keep_going = True
while keep_going:
    # Get user input to keep playing while true
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Call function to encrypt or decrypt
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    # Ask user if they want to encrypt or decrypt again
    go_again = input("Do you want to go again? Type yes or no.")
    if go_again == "no":
        keep_going = False




