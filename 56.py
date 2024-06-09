import hashlib
import random

# Import necessary libraries

# Generate a random private key
private_key = random.randint(1, 1000)
def check(blinding_factor, private_key):
    try:
        a = pow(blinding_factor, -1, private_key)
    except:
        return False
    return True
# Define the blind signature function
def blind_signature(message):
    # Generate a random blinding factor
    blinding_factor = random.randint(1, 1000)
    while(check(blinding_factor, private_key) == False):
        blinding_factor = random.randint(1, 1000)
    # Blind the message
    blinded_message = (message * pow(blinding_factor, private_key)) % private_key

    # Sign the blinded message
    signature = pow(blinded_message, private_key) % private_key

    # Check if the blinding factor is invertible
    if pow(blinding_factor, -1, private_key) is None:
        raise ValueError("Blinding factor is not invertible for the given modulus")

    # Unblind the signature
    unblinded_signature = (signature * pow(blinding_factor, -1, private_key)) % private_key

    return unblinded_signature
def decrypt_blind_signature(blind_signature):
    # Decrypt the blind signature using the private key
    decrypted_signature = pow(blind_signature, private_key) % private_key

    return decrypted_signature

def decrypt_message(decrypted_signature):
    # Decrypt the decrypted signature to get the original message
    message = pow(decrypted_signature, -1, private_key) % private_key
    return message
# Test the blind signature function
message = hashlib.sha256(b"Hello, world!").hexdigest()
signature = blind_signature(int(message, 16))
print("Blind Signature:", signature)


# Decrypt the blind signature
decrypted_signature = decrypt_blind_signature(signature)
print("Decrypted Signature:", decrypted_signature)


# Decrypt the message
decrypted_message = decrypt_message(decrypted_signature)
print("Decrypted Message:", decrypted_message)
original_message = hex(decrypted_message)[2:]
original_message = bytes.fromhex(original_message).decode('utf-8', errors='ignore')
print("Original Message:", original_message)