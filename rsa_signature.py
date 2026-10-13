from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

# Step 1: Generate RSA keys
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

print("RSA keys generated successfully!")

# Step 2: Create the original message
message = b"Transfer $1000 to Mark"

print("Original message:", message.decode())

# Step 3: Sign the message using the private key
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("Digital signature created successfully!")

# Step 4: Verify the original message
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
    print("Original message verification: VALID")
except InvalidSignature:
    print("Original message verification: INVALID")

# Step 5: Modify the message
modified_message = b"Transfer $1000 to Oscar"

print("Modified message:", modified_message.decode())

# Step 6: Verify the modified message
try:
    public_key.verify(
        signature,
        modified_message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Modified message verification: VALID")
except InvalidSignature:
    print("Modified message verification: INVALID")
