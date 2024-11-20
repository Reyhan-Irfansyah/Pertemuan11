def beaufort_encrypt(plaintext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaintext = plaintext.upper().replace(" ", "")  # Remove spaces and convert to uppercase
    key = key.upper().replace(" ", "")  # Remove spaces and convert to uppercase
    encrypted_text = []
    key_index = 0
    for char in plaintext:
        if char in alphabet:
            plaintext_index = alphabet.index(char)
            key_index_in_alphabet = alphabet.index(key[key_index % len(key)])
            encrypted_char = alphabet[(key_index_in_alphabet - plaintext_index) % 26]
            encrypted_text.append(encrypted_char)
            key_index += 1  # Move to the next character in the key
    return ''.join(encrypted_text)

def beaufort_decrypt(ciphertext, key):
    # Decryption is the same as encryption in Beaufort cipher.
    return beaufort_encrypt(ciphertext, key)

# Example usage
plaintext = "HELLO WORLD"
key = "KEY"
# Encryption
encrypted = beaufort_encrypt(plaintext, key)
print(f"Encrypted: {encrypted}")
# Decryption
decrypted = beaufort_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")