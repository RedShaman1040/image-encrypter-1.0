from cryptography.fernet import Fernet
from PIL import Image
import io

def generate_key():
    return Fernet.generate_key()

def encrypt_image(image_path, key):
    cipher = Fernet(key)
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
    encrypted_data = cipher.encrypt(image_data)
    return encrypted_data

def decrypt_image(encrypted_data, key):
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data

def save_image(image_data, image_path):
    with open(image_path, "wb") as image_file:
        image_file.write(image_data)

def main():
    key = generate_key()
    print("La clave de encriptación es:", key.decode())

    while True:
        print("\nSeleccione una opción:")
        print("1. Encriptar imagen")
        print("2. Desencriptar imagen")
        print("3. Salir")
        choice = input("Opción: ")

        if choice == "1":
            image_path = input("Ingrese la ruta de la imagen a encriptar: ")
            encrypted_data = encrypt_image(image_path, key)
            encrypted_image_path = input("Ingrese la ruta donde guardar la imagen encriptada: ")
            save_image(encrypted_data, encrypted_image_path)
            print("¡Imagen encriptada y guardada exitosamente!")

        elif choice == "2":
            encrypted_image_path = input("Ingrese la ruta de la imagen encriptada: ")
            with open(encrypted_image_path, "rb") as encrypted_image_file:
                encrypted_data = encrypted_image_file.read()
            decrypted_data = decrypt_image(encrypted_data, key)
            decrypted_image_path = input("Ingrese la ruta donde guardar la imagen desencriptada: ")
            save_image(decrypted_data, decrypted_image_path)
            print("¡Imagen desencriptada y guardada exitosamente!")

        elif choice == "3":
            print("¡Adiós!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
