def generate_vigenere_table():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    table = []
    for i in range(26):
        shifted_alphabet = alphabet[i:] + alphabet[:i]
        table.append(shifted_alphabet)
    return table

def vigenere_encrypt(plaintext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaintext = plaintext.upper().replace(" ", "")  # Remove spaces and convert to uppercase
    key = key.upper().replace(" ", "")  # Remove spaces and convert to uppercase
    encrypted_text = []
    key_index = 0
    # Generate Vigenère cipher table
    table = generate_vigenere_table()
    for char in plaintext:
        if char in alphabet:
            row = alphabet.index(char)
            col = alphabet.index(key[key_index % len(key)])
            encrypted_char = table[row][col]
            encrypted_text.append(encrypted_char)
            key_index += 1  # Move to the next character in the key
    return ''.join(encrypted_text)

def vigenere_decrypt(ciphertext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ciphertext.upper().replace(" ", "")  # Remove spaces and convert to uppercase
    key = key.upper().replace(" ", "")  # Remove spaces and convert to uppercase
    decrypted_text = []
    key_index = 0
    # Generate Vigenère cipher table
    table = generate_vigenere_table()
    for char in ciphertext:
        if char in alphabet:
            row = alphabet.index(key[key_index % len(key)])
            col = table[row].index(char)
            decrypted_char = alphabet[col]
            decrypted_text.append(decrypted_char)
            key_index += 1  # Move to the next character in the key
    return ''.join(decrypted_text)

# Example usage
plaintext = "BOBOLJAMSATU"
key = "KEY"
# Encryption
encrypted = vigenere_encrypt(plaintext, key)
print(f"Encrypted: {encrypted}")
# Decryption
decrypted = vigenere_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")