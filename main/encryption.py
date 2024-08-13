  
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_password(password, key):
    return Fernet(key).encrypt(password.encode())

def decrypt_password(encrypted_password, key):
    return Fernet(key).decrypt(encrypted_password).decode()


#More function will be added here
