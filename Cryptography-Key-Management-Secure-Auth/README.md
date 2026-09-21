# Cryptography, Key Management & Secure Auth

This project demonstrates secure cryptographic implementations in Python.

## Implementations

### 1. AES-256-GCM

File: `aes_gcm.py`

Demonstrates:

- AES-256 encryption
- AES-GCM authenticated encryption
- Random 96-bit IV generation
- Additional Authenticated Data (AAD)
- Encryption and decryption verification

### 2. RSA-2048 Digital Signature

File: `rsa_signature.py`

Demonstrates:

- RSA-2048 key generation
- RSA-PSS digital signatures
- SHA-256 hashing
- Signature verification
- Message integrity and authenticity verification

### 3. bcrypt Password Hashing

File: `password_hash.py`

Demonstrates:

- bcrypt password hashing
- Automatic random salt generation
- Work factor 12
- Correct password verification
- Incorrect password rejection

### 4. Secure Key Rotation

File: `key_rotation.py`

Demonstrates:

- Key versioning
- New key generation
- Key rotation
- Controlled retention of previous key versions

## Project Structure

```text
Cryptography-Key-Management-Secure-Auth/
│
├── aes_gcm.py
├── rsa_signature.py
├── password_hash.py
├── key_rotation.py
├── README.md
├── SECURITY.md
└── screenshots/
    ├── aes-output.png
    ├── rsa-output.png
    └── bcrypt-output.png