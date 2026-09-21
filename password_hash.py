import bcrypt


password = b"MySecurePassword123!"

# Generate a random salt and create bcrypt hash
hashed_password = bcrypt.hashpw(password, bcrypt.gensalt(rounds=12))

print("=== bcrypt Password Hashing ===")
print("Work factor: 12")
print("Password hash:", hashed_password.decode())

# Verify correct password
if bcrypt.checkpw(password, hashed_password):
    print("Correct password verification: SUCCESS")
else:
    print("Correct password verification: FAILED")

# Verify incorrect password
wrong_password = b"WrongPassword123!"

if bcrypt.checkpw(wrong_password, hashed_password):
    print("Incorrect password verification: FAILED")
else:
    print("Incorrect password verification: SUCCESS - password rejected")