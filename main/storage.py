import os
import json

def get_storage_path():
    # Get the user's home directory
    home_dir = os.path.expanduser("~")
    
    # Define the path to the .vaultcli directory
    storage_dir = os.path.join(home_dir, ".vaultcli")
    
    # Create the directory if it doesn't exist
    os.makedirs(storage_dir, exist_ok=True)
    
    # Return the full path to the password.json file
    return os.path.join(storage_dir, "password.json")


#TODO: Define the functions to save and load the passwords