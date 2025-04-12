import json
import os


def edit_settings():
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "config.json")


    if not os.path.exists(config_path):
        print("Config file not found!")
        return


    with open(config_path, 'r') as f:
        config = json.load(f)


    print(f"Current Token: {config.get('token', 'Not Set')}")
    print(f"Current Prefix: {config.get('prefix', 'Not Set')}")


    choice = input("Do you want to edit the token or prefix? (t/p): ").strip().lower()

    if choice == 't':
        
        new_token = input("Enter new token: ").strip()
        config['token'] = new_token
        print("Token updated successfully.")
    elif choice == 'p':

        new_prefix = input("Enter new prefix: ").strip()
        config['prefix'] = new_prefix
        print("Prefix updated successfully.")
    else:
        print("Invalid choice. No changes made.")


    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)
    print("Settings saved successfully.")


edit_settings()
