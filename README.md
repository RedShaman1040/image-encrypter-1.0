# image-encrypter-1.0
This Python application allows users to encrypt and decrypt images using the Fernet symmetric encryption from the cryptography library. The program provides a simple command-line interface for interacting with the encryption and decryption functionality.

### How to use it?

1. **Running the program:** When you run the program, a unique encryption key will be generated and displayed on the screen. This key is necessary for encrypting and decrypting images, so make sure to save it securely.

2. **Interactive menu:** The program presents an interactive menu with the following options:
   - **Encrypt image:** Allows you to select an image on your computer to encrypt. You need to enter the path of the image and the path where you want to save the encrypted image.
   - **Decrypt image:** Allows you to select an encrypted image to decrypt. You need to enter the path of the encrypted image and the path where you want to save the decrypted image.
   - **Exit:** Closes the program.

3. **Encryption and decryption:** Once you select an option, the program will encrypt or decrypt the image according to your choice and save the result in the specified path.

### What can it be used for?

1. **Data security:** You can use the program to encrypt images and protect them against unauthorized access. This is useful if you need to send sensitive images via email or store them in a public location.

2. **Privacy:** By encrypting your images, you can keep their content private and protect it from unwanted viewers.

3. **Secure transfer:** If you need to transfer images over the internet, encryption can ensure that the data is not intercepted or modified during the transfer.

In summary, the image encryption program is a useful tool for protecting your images and ensuring the privacy and security of your visual data.

# Installation
*Clone the repository:*
bash

    git clone https://github.com/your-username/image-encryption-app.git
*Install the required libraries:*
bash

    pip install -r requirements.txt

# Usage
*Run the program:*
bash

    python image_encryption_app.py
Follow the on-screen instructions to encrypt or decrypt images.
