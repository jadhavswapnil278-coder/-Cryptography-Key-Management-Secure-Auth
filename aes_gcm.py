from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import base64


# Generate a random 256-bit AES key
key = AESGCM.generate_key(bit_length=256)

# Create AES-GCM cipher
aes = AESGCM(key)

# Random 96-bit IV (recommended size for GCM)
iv = os.urandom(12)

# Data to encrypt
plaintext = b"Confidential Internship Data"

# Additional authenticated data
aad = b"OWASP-Crypto-Task"

# Encrypt
ciphertext = aes.encrypt(iv, plaintext, aad)

print("=== AES-256-GCM Encryption ===")
print("Key:", base64.b64encode(key).decode())
print("Random IV:", base64.b64encode(iv).decode())
print("Ciphertext:", base64.b64encode(ciphertext).decode())

# Decrypt
decrypted = aes.decrypt(iv, ciphertext, aad)

print("\n=== AES-256-GCM Decryption ===")
print("Decrypted Data:", decrypted.decode())

# Verification
if decrypted == plaintext:
    print("\nAES-256-GCM encryption/decryption successful!")