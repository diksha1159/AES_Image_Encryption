# AES_Image_Encryption
thinking of AES encryption as putting your image in a secure digital safe, try this repo

# AES Image Encryption Project

## Overview
This project focuses on encrypting and decrypting images using the Advanced Encryption Standard (AES) algorithm in Python. The implementation utilizes the `Pillow` library for image processing and the `pycryptodome` library for AES encryption. The encryption is done in Cipher Block Chaining (CBC) mode, and a random key and Initialization Vector (IV) are generated for enhanced security.

## Prerequisites
Ensure that you have the required libraries installed before running the code:

```bash
pip install Pillow
pip install pycryptodome
```

## Project Structure

### `main.py`
The main script, `main.py`, encompasses the following functionalities:
- Validates image files
- Generates a random key and IV
- Derives a password-based key using PBKDF2
- Calculates HMAC for data integrity

#### Running the Script
Execute the script by navigating to the directory where `main.py` is saved and using the following command:

```bash
python main.py
```

### `image_crypto.py`
The second script, `image_crypto.py`, provides a simplified approach to image encryption and decryption using the `pycryptodome` module. However, this script is currently not working as intended.

## Usage

### 1. Encrypting an Image
1. Run the `main.py` script and provide the path to the image when prompted.
2. The script will generate a random key and IV, encrypt the image, and save the encrypted image.

### 2. Decrypting an Image
1. After encrypting an image with `main.py`, use the provided key and IV to decrypt the image using the `main.py` script.

### 3. Troubleshooting `image_crypto.py`
If you encounter issues with the `image_crypto.py` script, consider reviewing and adjusting the code based on specific requirements. Thoroughly test the script with various scenarios to ensure correct functionality.

## Important Note
This example assumes the use of a random 128-bit key for AES encryption. In a real-world scenario, key management is crucial, and secure methods for key generation, storage, and exchange should be considered.

Feel free to adapt the code based on your project's requirements and conduct extensive testing to ensure its reliability.