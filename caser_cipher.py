#Python program to Encrypt and Decrypt the text given by the user using Caser Cipher Algorithm

def caesar_encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            base = ord('a') if char.islower() else ord('A')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            # Non-alphabetic characters are added unchanged
            encrypted_text += char

    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)  # Decrypting is just encrypting with a negative shift

# Main program
if __name__ == "__main__":
    while True:
        print("\n  CAESAR CIPHER  ")
        print("DO YOU WANT TO ENCRYPT OR DECRYPT THE MESSAGE? SELECT THE OPTIONS BELOW.")
        print("1. Encryption")
        print("2. Decryption")
        print("3. EXIT")
        
        action = input("Enter your choice: ").strip()

        if action == '1':
            text = input("Enter the text to encrypt: \n")
            shift = int(input("Enter the shift value: \n")) % 26  # Normalize shift
            encrypted = caesar_encrypt(text, shift)
            print(f"Encrypted text: {encrypted}\n\n")

        elif action == '2':
            text = input("Enter the text to decrypt: \n")
            shift = int(input("Enter the shift value: \n")) % 26  # Normalize shift
            decrypted = caesar_decrypt(text, shift)
            print(f"Decrypted text: {decrypted}\n\n")

        elif action == '3':
            print("Exiting the program.")
            break  # Exiting the loop and end the program

        else:
            print("Invalid option. Please choose '1' to encrypt, '2' to decrypt, or '3' to quit.")
            continue  # Continue to the next iteration of the loop

        # Asking the user if they want to continue
        continue_choice = input("Do you want to continue? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Exiting the program.")
            break  # Exiting the loop and end the program
        