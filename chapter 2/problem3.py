import os

def list_directory_contents(directory):
    try:
        contents = os.listdir(directory)
        print(f"Contents of '{directory}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print("Error: Directory not found.")
    except PermissionError:
        print("Error: Permission denied.")

# Example usage
directory_path = 'chapter2'
list_directory_contents(directory_path)
 