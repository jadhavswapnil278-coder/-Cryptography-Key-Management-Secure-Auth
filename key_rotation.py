from cryptography.fernet import Fernet


# Simulated key store.
# In production, use a secrets manager or HSM.
key_store = {}


def generate_key(version):
    key = Fernet.generate_key()
    key_store[version] = key
    return key


def rotate_key(current_version):
    new_version = current_version + 1
    new_key = generate_key(new_version)

    print("=== Secure Key Rotation Demo ===")
    print("Previous key version:", current_version)
    print("New key version:", new_version)
    print("New key generated successfully!")
    print("Old key retained for controlled migration/rollback.")


# Initial key
generate_key(1)

# Rotate to version 2
rotate_key(1)

print("\nKey versions currently managed:", list(key_store.keys()))