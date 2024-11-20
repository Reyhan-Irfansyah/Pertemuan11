def autokey_encrypt(plaintext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaintext = plaintext.upper().replace(" ", "")  # Remove spaces and convert to uppercase
    key = key.upper().replace(" ", "")  # Remove spaces and convert to uppercase
    ciphertext = []
    # The key stream is the key followed by the plaintext
    key_stream = key + plaintext
    for i in range(len(plaintext)):
        if plaintext[i] in alphabet:
            plaintext_index = alphabet.index(plaintext[i])
            key_index = alphabet.index(key_stream[i])
            encrypted_char = alphabet[(plaintext_index + key_index) % 26]
            ciphertext.append(encrypted_char)
    return ''.join(ciphertext)

def autokey_decrypt(ciphertext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ciphertext.upper().replace(" ", "")  # Remove spaces and convert to uppercase
    key = key.upper().replace(" ", "")  # Remove spaces and convert to uppercase
    plaintext = []
    # The key stream is the key followed by the ciphertext (we'll rebuild the key stream from ciphertext)
    key_stream = key
    for i in range(len(ciphertext)):
        if ciphertext[i] in alphabet:
            ciphertext_index = alphabet.index(ciphertext[i])
            key_index = alphabet.index(key_stream[i])
            decrypted_char = alphabet[(ciphertext_index - key_index) % 26]
            plaintext.append(decrypted_char)
            # Update the key stream with the decrypted letter for the next step
            key_stream += decrypted_char
    return ''.join(plaintext)

# Example usage
plaintext = "wearediscoveredsaveyourself"
key = "deceptive"
# Encryption
encrypted = autokey_encrypt(plaintext, key)
print(f"Encrypted: {encrypted}")
# Decryption
decrypted = autokey_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")