# Feistel Shield

### By: Yash Mhaskar | Date: 2 - Oct - 24

This is a simple implementation of the Feistel Network used in DES. 

--------

## Usage

        python3 main.py

- Enter the number of rounds.
- Enter a message (the plaintext).
- The program will calculate the ciphertext as the per the number of rounds.
- The ciphertext will be displayed.
- The plaintext will be calculated based on the ciphertext.

---------

## Don't use this cipher in production software

This cipher is a simple demonstration. Not to be used to secure critical data.

- Poor choice of the round function. In the program I have just used the XOR operation as the round function.
- Doesn't use 256-bit keys. Program creates keys as long as the plaintext which in most cases will be too short to be secure.
- Program takes input a message, encrypts the message and also displays the plaintext afterwards.
- No message integrity. Doesn't use message authenication codes.
- The keys are not CSPRNs. Keys are generated by the randint function in the random  library in python. The keys can be predicted.
