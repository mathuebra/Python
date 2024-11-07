import os

# Define the base folder path and expands the user's home directory symbol (~)
base_folder_path = os.path.expanduser("~/EngComp/")

# Ensure the base folder path exists
if not os.path.exists(base_folder_path):
    os.makedirs(base_folder_path)

# Loop to get user input and create folders
while True:
    folder_name = input("Digite o nome da pasta (ou 'exit' para sair): ")
    if folder_name.lower() == "exit":
        break
    
    # Construct the full folder path
    folder_path = os.path.join(base_folder_path, folder_name)
    
    # Create the folder if it does not exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Pasta '{folder_path}' criada com sucesso.")
    else:
        print(f"Pasta '{folder_path}' já existe.")
