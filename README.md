# RSA Digital Signature Using Python

## Project Description

This project implements a digital signature using the RSA algorithm in Python. It demonstrates how digital signatures can verify the authenticity and integrity of a message.

The project was developed as part of the Software Security course (SDEV 4303), Chapter 2: Cryptographic Tools.

## Technologies Used

- Python
- Cryptography Library
- RSA Algorithm
- SHA-256 Hash Function
- PSS Padding

## How the Program Works

1. Generates an RSA public and private key pair.
2. Creates an original message.
3. Signs the message using the private key.
4. Verifies the signature using the public key.
5. Modifies the message and checks the signature again.

## How to Run

**1. Install the required library:**

```bash
python -m pip install cryptography
```

**2. Run the Python file:**

```bash
python rsa_signature.py
```

## Expected Output

```text
RSA keys generated successfully!
Original message: Transfer $1000 to Mark
Digital signature created successfully!
Original message verification: VALID
Modified message: Transfer $1000 to Oscar
Modified message verification: INVALID
```

## Results

The original message passes signature verification because it has not been modified.

After changing the receiver's name from Mark to Oscar, verification fails because the original signature does not match the modified message.

This demonstrates how RSA digital signatures can help verify message authenticity and detect unauthorized changes.

## Course Information

- **Course:** Software Security
- **Course Code:** SDEV 4303
- **Chapter:** 02 – Cryptographic Tools
- **Instructor:** Dr. Abdelkareem Alashqar
- **Academic Year:** 2026/2027
