# This file contains the functions that are used to manage the passwords

import encryption

key = encryption.generate_key()

def add_password(servic, username, password):
    encrypted_password = encryption.encrypt_password(password, key)
    #TODO: Save function will be implemented later
    print(f"Password for {username} on {servic} added successfully")

def view_password():
    pass
    #TODO: View function will be implemented later
    
#* The functions will be implemented later