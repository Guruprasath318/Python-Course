from cryptography.fernet import Fernet

# Generate a key (or load your key from a secure place)
key = Fernet.generate_key()

cipher = Fernet(key)

# Step 2: Encrypt the message
message = input("Enter the message to encrypt: ")
encrypted_message = cipher.encrypt(message.encode())
print("Encrypted:", encrypted_message)

# Step 3: Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message.decode())
print("Decrypted:", decrypted_message)


