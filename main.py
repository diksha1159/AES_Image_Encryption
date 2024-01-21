from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from PIL import Image
import os

def load_image(image_path):
    try:
        img = Image.open(image_path)
        img.verify()  # Check if the file is a valid image
        img.show()
        return img
    except Exception as e:
        print(f"Error loading the image: {e}")
        exit(1)

def generate_key(password, salt=b'salt123', iterations=1000000):
    return PBKDF2(password, salt=salt, dkLen=32, count=iterations)

def encrypt_image(image_path, password):
    iv = get_random_bytes(16)
    key = generate_key(password)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    with open(image_path, 'rb') as file:
        plaintext = file.read()

    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    # Store IV and encrypted image together
    encrypted_data = iv + ciphertext

    # Create a directory to store encrypted images
    encrypted_dir = "encrypted_images"
    os.makedirs(encrypted_dir, exist_ok=True)

    encrypted_path = os.path.join(encrypted_dir, "encrypted_image.enc")
    with open(encrypted_path, 'wb') as file:
        file.write(encrypted_data)

def decrypt_image(encrypted_path, password):
    with open(encrypted_path, 'rb') as file:
        encrypted_data = file.read()

    # Extract IV and ciphertext
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]

    key = generate_key(password)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)

    # Create a directory to store decrypted images
    decrypted_dir = "decrypted_images"
    os.makedirs(decrypted_dir, exist_ok=True)

    decrypted_path = os.path.join(decrypted_dir, "decrypted_image.jpg")
    with open(decrypted_path, 'wb') as file:
        file.write(decrypted_data)

if __name__ == "__main__":
    image_path = input("Enter the path of the image: ")
    password = input("Enter your password: ")

    # Encrypt the image
    encrypt_image(image_path, password)
    print("Image encrypted successfully.")

    # Decrypt the image
    decrypt_image("encrypted_images/encrypted_image.enc", password)
    print("Image decrypted successfully.")
