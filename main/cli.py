
import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="VaultCLI",
        description= "Password Manager CLI")
    
    parser.add_argument("--action", choices=["add", "view"], help="Action to perform")
    #more arguments will be added here
    
    args = parser.parse_args()

    if args.action == "add":
        pass                   # Add password
    elif args.action == "view":
        pass                   # View password
    else:
        print("Invalid action")

if __name__ == "__main__":
    main()
