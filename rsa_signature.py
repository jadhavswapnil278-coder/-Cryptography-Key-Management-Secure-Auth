from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


# Generate RSA-2048 private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Generate public key
public_key = private_key.public_key()

# Message to sign
message = b"Secure authentication transaction"

# Create digital signature
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("=== RSA-2048 Digital Signature ===")
print("RSA key size: 2048 bits")
print("Signature generated successfully!")
print("Signature length:", len(signature), "bytes")

# Verify signature
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    print("Signature verification: SUCCESS")
    print("Message integrity and authenticity verified!")

except Exception:
    print("Signature verification: FAILED")