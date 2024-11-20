def encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Determine if character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Apply the shift, using modulo to wrap around the alphabet
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            ciphertext += shifted_char
        else:
            # Non-alphabetic characters remain unchanged
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Determine if character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Reverse the shift, using modulo to wrap around the alphabet
            shifted_char = chr((ord(char) - start - shift) % 26 + start)
            plaintext += shifted_char
        else:
            # Non-alphabetic characters remain unchanged
            plaintext += char
    return plaintext

# Example usage:
if __name__ == "__main__":
    text = "waktu kuliah jangan ngantuk"  # Text to encrypt
    shift_value = 3  # Caesar cipher shift value
    encrypted = encrypt(text, shift_value)
    print(f"Encrypted: {encrypted}")
    decrypted = decrypt(encrypted, shift_value)
    print(f"Decrypted: {decrypted}")