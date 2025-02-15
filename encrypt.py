import cv2
import os

def encrypt_image(image_path, message, key):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return
    
    d = {chr(i): i for i in range(255)}
    
    n, m, z = 0, 0, 0

    message += "\0"  # Append a null terminator to mark end of message

    for char in message:
        if n >= img.shape[0] or m >= img.shape[1]:  # Prevent out-of-bounds error
            print("Error: Image too small for message!")
            return
        img[n, m, z] = (d[char] ^ key) % 256  # Apply XOR and keep within 0-255
        n += 1
        m += 1
        z = (z + 1) % 3
    
    encrypted_image_path = "encryptedImage.png"
    cv2.imwrite(encrypted_image_path, img)
    print("Message encrypted and saved as encryptedImage.png")

    with open("encryption_key.txt", "w") as f:
        f.write(str(key))  # Save key securely

if __name__ == "__main__":
    image_path = "mypic.png"  # Replace with the correct image path
    message = input("Enter secret message: ")
    key = int(input("Enter an encryption key (integer): "))
    encrypt_image(image_path, message, key)
