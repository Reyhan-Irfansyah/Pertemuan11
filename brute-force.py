def caesar_cipher_decrypt(ciphertext, shift):
    decrypted_text = []
    for char in ciphertext:
        if char.isalpha():
            # Shift the character and handle wraparound using modulus
            shift_base = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

def brute_force_caesar(ciphertext):
    print("Brute-forcing Caesar Cipher decryption:")
    for shift in range(26):  # There are 26 possible shifts in Caesar cipher
        decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")

# Example usage
ciphertext = "Uifsf jt b tfdsfu dpef!"  # "There is a secret code!"
brute_force_caesar(ciphertext)