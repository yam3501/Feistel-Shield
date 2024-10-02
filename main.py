import random
ROUNDS = int(input("Enter rounds: "))                                   # Total rounds

def rand_key(x):                                                        # Func. to generate random key
    return ''.join(str(random.randint(0, 1)) for _ in range(x))

def xor(a, b):                                                          # Func. to perform XOR operation
    return ''.join('0' if a[i] == b[i] else '1' for i in range(len(a)))

def binary_to_decimal(binary):                                          # Func. to convert from bin to dec
    return int(binary, 2)

def encryption(l, r):                                                   # Encryption function
    for round in range(ROUNDS):
        round_function = xor(r, keys[round])
        temp = xor(round_function, l)
        l, r = r, temp
    return l, r

def decryption(l, r):                                                   # Decryption function
    for round in reversed(range(ROUNDS)):
        round_function = xor(r, keys[round])
        temp = xor(round_function, l)
        l, r = r, temp
    return l, r

# Driver Code

plaintext = input("Enter message: ")
print("Plaintext is: ", plaintext, "\n")

plaintext_in_ascii = [ord(x) for x in plaintext] 
plaintext_in_bin = [format(y, '08b') for y in plaintext_in_ascii]
plaintext_in_bin = "".join(plaintext_in_bin)

n = len(plaintext_in_bin) // 2
left_init = plaintext_in_bin[:n]
right_init = plaintext_in_bin[n:]
m = len(right_init)
keys = [rand_key(m) for _ in range(ROUNDS)]

final_left, final_right = encryption(left_init, right_init)
bin_data = final_left + final_right

str_data = ''
for i in range(0, len(bin_data), 8):
    temp_data = bin_data[i:i + 8]
    decimal_data = binary_to_decimal(temp_data)
    str_data += chr(decimal_data)

print("Cipher Text: ", str_data, "\n")

calculated_right, calculated_left = decryption(final_right, final_left)

calculated_plaintext = calculated_left + calculated_right
decoded_data = ''
for i in range(0, len(calculated_plaintext), 8):
    temp_data = calculated_plaintext[i:i + 8]
    decimal_data = binary_to_decimal(temp_data)
    decoded_data += chr(decimal_data)

print("Retrieved Plain Text is: ", decoded_data)