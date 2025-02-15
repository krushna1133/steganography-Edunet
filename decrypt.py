import cv2
import os

def decrypt_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return
    
    c = {i: chr(i) for i in range(255)}
    
    n, m, z = 0, 0, 0
    message = ""

    try:
        with open("encryption_key.txt", "r") as f:
            key = int(f.read().strip())  # Read stored key
    except FileNotFoundError:
        print("Error: Encryption key file not found!")
        return
    
    entered_key = int(input("Enter the encryption key: "))
    if entered_key == key:
        while n < img.shape[0] and m < img.shape[1]:  # Prevent out-of-bounds
            char = c[(img[n, m, z] ^ key) % 256]  # Reverse XOR and keep within 0-255
            if char == "\0":  # Stop when end-of-message marker is reached
                break
            message += char
            n += 1
            m += 1
            z = (z + 1) % 3
        
        print("Decrypted message:", message)
    else:
        print("Incorrect key! Access denied.")

if __name__ == "__main__":
    decrypt_image("encryptedImage.png")
