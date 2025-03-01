# Caesar Cipher Encryption and Decryption Program

## Overview

The **Caesar Cipher** is one of the simplest and most well-known encryption techniques. This Python program implements the Caesar Cipher algorithm, allowing users to encrypt and decrypt messages using a specified shift value. The algorithm works by shifting each letter in the plaintext by a fixed number of positions down the alphabet. For instance, with a shift of 3, 'A' becomes 'D', 'B' becomes 'E', and so forth. Non-alphabetic characters remain unchanged.

## Features

- **Encryption**: Users can input a message and a shift value to encrypt the text.
- **Decryption**: Users can input an encrypted message and the same shift value to retrieve the original text.
- **User -Friendly Interface**: A command-line interface guides users through the encryption and decryption process.
- **Continue or Exit**: After each operation, users can choose to continue or exit the program, facilitating multiple operations in a single session.
- **Input Validation**: The program normalizes the shift value to ensure it remains within the range of 0-25, accommodating larger shift values.

## How to Use

1. **Run the Program**: Execute the script in a Python environment. Ensure that Python 3.x is installed on your machine.

2. **Select an Option**: The program will display a menu with three options:
   - **1**: Encrypt a message
   - **2**: Decrypt a message
   - **3**: Exit the program

3. **Input Text and Shift Value**:
   - For encryption, enter the text you wish to encrypt and the desired shift value.
   - For decryption, enter the encrypted text and the same shift value used for encryption.

4. **Continue or Exit**: After performing an operation, you will be prompted to continue. Enter 'yes' to perform another operation or 'no' to exit the program.

## Example Usage

```plaintext
  CAESAR CIPHER  
DO YOU WANT TO ENCRYPT OR DECRYPT THE MESSAGE? SELECT THE OPTIONS BELOW.
1. Encryption
2. Decryption
3. EXIT
Enter your choice: 1
Enter the text to encrypt: Hello, World!
Enter the shift value: 3
Encrypted text: Khoor, Zruog!

Do you want to continue? (yes/no): yes

Enter your choice: 2
Enter the text to decrypt: Khoor, Zruog!
Enter the shift value: 3
Decrypted text: Hello, World!

Do you want to continue? (yes/no): no
Exiting the program.
