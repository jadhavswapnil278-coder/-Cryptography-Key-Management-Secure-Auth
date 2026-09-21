# Security Best Practices

## 1. AES-256-GCM

- Use AES-256-GCM for authenticated symmetric encryption.
- Generate a unique random IV for every encryption operation.
- Never reuse the same IV with the same AES-GCM key.
- Store encryption keys in a secure secrets manager.
- Never hard-code production encryption keys in source code.

## 2. RSA-2048

- Use RSA keys of at least 2048 bits.
- Protect private keys from unauthorized access.
- Distribute only the public key.
- Use secure signature algorithms such as RSA-PSS with SHA-256.
- Rotate keys according to organizational security policy.

## 3. Password Security

- Passwords must never be stored in plaintext.
- Use bcrypt or another approved password hashing algorithm.
- Use an appropriate work factor and review it periodically.
- Generate a unique random salt for each password.
- Never log plaintext passwords or password hashes unnecessarily.

## 4. Secret and Key Storage

Production secrets should not be stored directly in source code or Git repositories.

Recommended options include:

- Environment variables for development configuration
- Cloud secret managers
- Hardware Security Modules (HSMs)
- Dedicated enterprise key-management systems

Access to secrets should follow least-privilege principles.

## 5. Key Rotation

Keys should have identifiable versions.

Example:

- Version 1 → Current/previous key
- Version 2 → Newly rotated key

During rotation:

1. Generate a new cryptographically secure key.
2. Assign a new key version.
3. Start using the new key for new encryption operations.
4. Retain the previous key only as long as required to decrypt/migrate existing data.
5. Re-encrypt data where appropriate.
6. Retire and securely destroy the old key when no longer required.

## 6. Source Control

Never commit:

- Production private keys
- API keys
- Passwords
- Database credentials
- Cloud access tokens
- Encryption secrets

Use `.gitignore` to prevent accidental secret commits.